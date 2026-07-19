import traceback
import streamlit as st

from chatbot import get_response
from emergency import is_emergency
from response_formatter import format_response


def show_chat():

    # -----------------------------
    # Initialize Chat History
    # -----------------------------
    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 **Welcome to the AI Symptom Checking Chatbot!**\n\n"
                    "I'm here to help you understand your symptoms.\n\n"
                    "Describe your symptoms to begin."
                )
            }
        ]

    # -----------------------------
    # Display Previous Messages
    # -----------------------------
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -----------------------------
    # Chat Input
    # -----------------------------
    prompt = st.chat_input("Describe your symptoms...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # -----------------------------
        # Emergency Detection
        # -----------------------------
        if is_emergency(prompt):

            warning_message = (
                "🚨 **Possible Medical Emergency Detected**\n\n"
                "Please seek immediate medical attention."
            )

            with st.chat_message("assistant", avatar="🩺"):
                st.error(warning_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": warning_message
                }
            )

            st.stop()

        # -----------------------------
        # Build Conversation
        # -----------------------------
        conversation = []

        for msg in st.session_state.messages:

            conversation.append(
                {
                    "role": msg["role"],
                    "parts": [
                        {
                            "text": msg["content"]
                        }
                    ]
                }
            )

        # -----------------------------
        # AI Response
        # -----------------------------
        with st.chat_message("assistant", avatar="🩺"):

            with st.spinner("🧠 Analyzing symptoms..."):

                try:

                    raw_answer = get_response(conversation)

                    answer = format_response(raw_answer)

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    traceback.print_exc()

                    st.error(f"Error: {e}")