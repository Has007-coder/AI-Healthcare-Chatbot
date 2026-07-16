from google import genai
from google.genai import types

from config import GOOGLE_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT
from symptom_checker import analyze_symptoms
from follow_up import generate_follow_up_questions
from intent_detector import detect_intent

# Create Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)


def get_response(conversation):
    """
    Generate a healthcare chatbot response.
    """

    # Combine all user messages
    all_user_messages = ""

    for message in conversation:
        if message["role"] == "user":
            all_user_messages += message["parts"][0]["text"] + "\n"
            # Get the latest user message
latest_message = ""

for message in reversed(conversation):
    if message["role"] == "user":
        latest_message = message["parts"][0]["text"]
        break

# Detect user intent
intent = detect_intent(latest_message)
# Greeting
if intent == "greeting":
    return (
        "👋 Hello! Welcome to MedAssist AI.\n\n"
        "I'm here to answer general health questions and provide educational information about symptoms.\n\n"
        "How can I help you today?"
    )

# Thank you
if intent == "thanks":
    return (
        "😊 You're welcome! I'm glad I could help. "
        "Feel free to ask if you have any other health-related questions."
    )

# Goodbye
if intent == "goodbye":
    return (
        "👋 Take care! Wishing you good health. "
        "Have a wonderful day!"
    )

# General health question
if intent == "health_question":

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=latest_message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    return response.text

    # Analyze conversation
    symptom_analysis = analyze_symptoms(all_user_messages)

    # Debug output
    print("\n===== Conversation =====")
    print(all_user_messages)

    print("\n===== Analysis =====")
    print(symptom_analysis)

    # Generate follow-up questions
    questions = generate_follow_up_questions(symptom_analysis)

    if questions:
        return (
            "I can help you better with a little more information:\n\n"
            + "\n".join(
                [
                    f"{i+1}. {question}"
                    for i, question in enumerate(questions)
                ]
            )
        )

    enhanced_conversation = conversation.copy()

    enhanced_conversation.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": f"""
Patient Information Summary

Symptoms:
{', '.join(symptom_analysis['symptoms'])}

Duration:
{symptom_analysis['duration']}

Severity:
{symptom_analysis['severity']}

Age:
{symptom_analysis['age']}

Gender:
{symptom_analysis['gender']}

Provide:
1. Possible causes (not a diagnosis).
2. General home-care advice.
3. Red flags that require immediate medical attention.
4. Mention that this is educational information and not a substitute for a doctor.
"""
                }
            ]
        }
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=enhanced_conversation,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    return response.text