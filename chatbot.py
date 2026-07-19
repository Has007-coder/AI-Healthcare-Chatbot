from google import genai
from google.genai import types

from config import GOOGLE_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT

from emergency import is_emergency
from intent_detector import detect_intent
from symptom_checker import analyze_symptoms
from follow_up import generate_follow_up_questions

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

# ----------------------------------------
# Gemini Client
# ----------------------------------------

client = genai.Client(
    api_key=GOOGLE_API_KEY
)


# ----------------------------------------
# Main Chatbot Function
# ----------------------------------------

def get_response(conversation):

    latest_message = ""

    for message in conversation:

        if message["role"] == "user":
            latest_message = message["parts"][0]["text"]


    # ----------------------------------------
    # Emergency Detection
    # ----------------------------------------

    if is_emergency(latest_message):

        return (
            "⚠️ Your symptoms may indicate a medical emergency.\n\n"
            "Please seek immediate medical attention or contact your local emergency services immediately."
        )


    # ----------------------------------------
    # Intent Detection
    # ----------------------------------------

    intent = detect_intent(latest_message)


    if intent == "greeting":

        return (
            "👋 Hello! I'm your AI Healthcare Assistant.\n\n"
            "How can I help you today?"
        )


    if intent == "thanks":

        return (
            "😊 You're welcome! Stay healthy!"
        )


    if intent == "goodbye":

        clear_memory()
        clear_waiting()

        return (
            "👋 Take care! Wishing you good health."
        )
        # ----------------------------------------
    # Waiting for Missing Information
    # ----------------------------------------

    waiting = get_waiting()

    if waiting:

        update_memory({
            waiting: latest_message
        })

        clear_waiting()


    # ----------------------------------------
    # Detect Symptoms
    # ----------------------------------------

    symptom_data = analyze_symptoms(latest_message)

    update_memory(symptom_data)

    # ----------------------------------------
    # Check Patient Memory
    # ----------------------------------------

    memory = get_memory()

    missing_information = get_missing_information(memory)


    # ----------------------------------------
    # Ask Follow-up Questions
    # ----------------------------------------

    if missing_information:

        next_field = missing_information[0]

        set_waiting(next_field)

        return generate_follow_up_questions(next_field)


    # ----------------------------------------
    # Generate AI Response
    # ----------------------------------------

    return generate_ai_response(conversation)
# ----------------------------------------
# Build Patient Context
# ----------------------------------------

def build_patient_context():
    """
    Build a summary of the patient's information
    collected during the conversation.
    """

    memory = get_memory()

    symptoms = ", ".join(memory["symptoms"]) if memory["symptoms"] else "Not provided"

    return f"""
Patient Information

Age: {memory.get("age") or "Not provided"}
Gender: {memory.get("gender") or "Not provided"}

Symptoms:
{symptoms}

Duration:
{memory.get("duration") or "Not provided"}

Severity:
{memory.get("severity") or "Not provided"}
"""
# ----------------------------------------
# Generate AI Response
# ----------------------------------------

def generate_ai_response(conversation):

    patient_context = build_patient_context()

    conversation_text = ""

    for message in conversation:

        role = message["role"]
        text = message["parts"][0]["text"]

        conversation_text += f"{role}: {text}\n"


    final_prompt = f"""
{patient_context}

Conversation:

{conversation_text}

Instructions:

You are an AI Healthcare Assistant.

Rules:

1. Give educational health information only.

2. Never diagnose diseases.

3. Never prescribe medicines.

4. Suggest safe self-care whenever appropriate.

5. Recommend visiting a healthcare professional if symptoms persist.

6. If symptoms appear dangerous, advise immediate medical attention.

Respond politely and professionally.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=final_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        if response and response.text:
            return response.text

        return "I couldn't generate a response."

    except Exception as e:

        print("Gemini Error:", e)

        return (
            "⚠️ Unable to connect to Gemini. "
            "Please try again."
        )