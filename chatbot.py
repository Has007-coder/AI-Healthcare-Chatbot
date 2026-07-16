from google import genai
from google.genai import types

from config import GOOGLE_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT
from symptom_checker import analyze_symptoms
from follow_up import generate_follow_up_questions
from intent_detector import detect_intent
from conversation_manager import get_missing_information
from patient_memory import (
    get_memory,
    update_memory,
    clear_memory
)

from conversation_state import (
    get_waiting,
    set_waiting,
    clear_waiting
)


conversation_history = []

# Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)


def get_response(conversation):
    """
    Generate a response for the healthcare chatbot.
    """

    # ----------------------------
    # Collect User Messages
    # ----------------------------
    all_user_messages = ""

    for message in conversation:
        if message["role"] == "user":
            all_user_messages += message["parts"][0]["text"] + "\n"

    latest_message = ""

    for message in reversed(conversation):
        if message["role"] == "user":
            latest_message = message["parts"][0]["text"]
            break

    # ----------------------------
    # Detect Intent
    # ----------------------------
    intent = detect_intent(latest_message)
    waiting = get_waiting()

    if waiting == "age":

       update_memory({
        "age": latest_message
    })

       clear_waiting()

       return (
         f"Thank you. I have recorded your age as {latest_message}."
    )

    # ----------------------------
    # Greeting
    # ----------------------------
    if intent == "greeting":
        return (
            "👋 Hello! Welcome to MedAssist AI.\n\n"
            "I'm here to answer general health questions and provide educational information.\n\n"
            "How can I help you today?"
        )

    # ----------------------------
    # Thank You
    # ----------------------------
    if intent == "thanks":
        return (
            "😊 You're welcome! Feel free to ask if you have any other health-related questions."
        )

    # ----------------------------
    # Goodbye
    # ----------------------------
    if intent == "goodbye":
        return (
            "👋 Take care! Wishing you good health."
        )

    # ----------------------------
    # General Health Question
    # ----------------------------
    if intent == "health_question":

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=conversation,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        return response.text

    # ----------------------------
    # Symptom Analysis
    # ----------------------------
    symptom_analysis = analyze_symptoms(all_user_messages)

    print("\n===== Conversation =====")
    print(all_user_messages)

    print("\n===== Analysis =====")
    print(symptom_analysis)

    missing = get_missing_information(symptom_analysis)

    # ----------------------------
    # Missing Information
    # ----------------------------
    if missing:

        questions = []

        if "symptoms" in missing:
            questions.append("What symptoms are you experiencing?")

        if "duration" in missing:
            questions.append("How long have you had these symptoms?")

        if "severity" in missing:
            questions.append(
                "Would you describe them as mild, moderate, or severe?"
            )
        if "age" in missing:
           set_waiting("age")
           questions.append("How old are you?")

        return (
            "I need a little more information before I can provide general health guidance.\n\n"
            + "\n".join(
                f"{i+1}. {q}"
                for i, q in enumerate(questions)
            )
        )

    # ----------------------------
    # Follow-up Questions
    # ----------------------------
    followup = generate_follow_up_questions(symptom_analysis)

    if followup:
        return (
            "I can help you better with a little more information:\n\n"
            + "\n".join(
                f"{i+1}. {q}"
                for i, q in enumerate(followup)
            )
        )

    # ----------------------------
    # Final Prompt
    # ----------------------------
    enhanced_prompt = f"""
Patient Information Summary

Symptoms:
{", ".join(symptom_analysis["symptoms"])}

Duration:
{symptom_analysis["duration"]}

Severity:
{symptom_analysis["severity"]}

Age:
{symptom_analysis["age"]}

Gender:
{symptom_analysis["gender"]}

Please provide:

1. Possible causes (not a diagnosis).
2. General home-care advice.
3. Red flags requiring immediate medical attention.
4. Mention this is educational information only.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=enhanced_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    return response.text