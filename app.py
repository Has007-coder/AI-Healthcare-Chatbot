import streamlit as st

from chatbot import get_response
from emergency import is_emergency
import traceback


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🩺",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("🩺 AI Healthcare Assistant")

st.caption(
    "Educational healthcare information powered by Gemini."
)


# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Hello! I'm your AI Healthcare Assistant.\n\n"
                "I can help explain symptoms, health topics, "
                "nutrition, and general healthcare information.\n\n"
                "How can I help you today?"
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
if prompt := st.chat_input("Describe your symptoms..."):


    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Display User Message
    with st.chat_message("user"):

        st.markdown(prompt)



    # -----------------------------
    # Emergency Detection
    # -----------------------------
    if is_emergency(prompt):

        warning_message = """
🚨 **Possible Medical Emergency Detected**

Your symptoms may require immediate medical attention.

Please contact your local emergency services or visit the nearest hospital immediately.

⚠️ This AI assistant cannot evaluate emergency situations.
"""

        with st.chat_message("assistant"):

            st.warning(warning_message)


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": warning_message
            }
        )


        st.stop()



    # -----------------------------
    # Build Conversation History
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
    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):

            try:

                answer = get_response(conversation)


                st.markdown(answer)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


            except Exception:
             st.exception(Exception)
             traceback.print_exc()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("🩺 Healthcare Assistant")


    st.write(
        """
This chatbot provides educational healthcare information only.

It cannot diagnose diseases or replace professional medical advice.
"""
    )


    st.markdown("---")


    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hello! I'm your AI Healthcare Assistant. "
                    "How can I help you today?"
                )
            }
        ]

        st.rerun()