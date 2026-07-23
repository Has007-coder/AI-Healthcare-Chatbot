import traceback
import streamlit as st

from chatbot import get_response
from emergency import is_emergency
from response_formatter import format_response

from components.styles import load_css

from conversation_history import (
    initialize_history,
    get_current_conversation,
    save_messages,
)


# -----------------------------------------
# Display Chat Messages
# -----------------------------------------
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# -----------------------------------------
# Generate AI Response
# -----------------------------------------
def generate_ai_response(prompt):

    # Emergency Detection
    if is_emergency(prompt):

        warning = (
            "🚨 **Possible Medical Emergency Detected**\n\n"
            "Please seek immediate medical attention immediately."
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": warning,
            }
        )

        save_messages(st.session_state.messages)
        st.rerun()

    history = []

    for msg in st.session_state.messages:
        history.append(
            {
                "role": msg["role"],
                "parts": [
                    {
                        "text": msg["content"]
                    }
                ],
            }
        )

    try:

        with st.spinner("🧠 Analyzing symptoms..."):
            raw_response = get_response(history)

        answer = format_response(raw_response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        save_messages(st.session_state.messages)
        st.rerun()

    except Exception as e:

        traceback.print_exc()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"❌ Error: {e}",
            }
        )

        save_messages(st.session_state.messages)
        st.rerun()


# -----------------------------------------
# Handle User Input
# -----------------------------------------
def handle_user_input():

    prompt = st.chat_input("Describe your symptoms...")

    if not prompt:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    save_messages(st.session_state.messages)

    generate_ai_response(prompt)


# -----------------------------------------
# Main Chat Page
# -----------------------------------------
def show_chat():

    initialize_history()
    load_css()

    conversation = get_current_conversation()

    if not conversation["messages"]:
        conversation["messages"] = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hello! I'm your AI Healthcare Assistant.\n\n"
                    "How can I help you today?"
                ),
            }
        ]

    st.session_state.messages = conversation["messages"]

    display_messages()

    handle_user_input()