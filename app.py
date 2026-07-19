import traceback
import streamlit as st

from chatbot import get_response
from emergency import is_emergency

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Symptom Checking Chatbot",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #F5F9FC;
}

/* Main Title */
h1 {
    color: red;
    font-size: 50px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EAF4FF;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: bold;
}

/* Chat Input */
[data-testid="stChatInput"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------
# Title
# -----------------------------
st.title("🩺 AI Symptom Checking Chatbot")

st.markdown("""
### Your Intelligent Healthcare Companion

Describe your symptoms, and I'll ask follow-up questions to better understand your condition and provide **educational health guidance**.

> ⚠️ **Disclaimer:** This chatbot does **not** diagnose diseases or replace professional medical advice.
""")
# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
       
  {
    "role": "assistant",
    "content": (
        "👋 **Welcome to the AI Symptom Checking Chatbot!**\n\n"
        "I'm here to help you understand your symptoms through an interactive conversation.\n\n"
        "**I can help you with:**\n"
        "• 🤒 Symptom assessment\n"
        "• ❓ Follow-up questions\n"
        "• 🚨 Emergency symptom detection\n"
        "• 📚 Educational health information\n\n"
        "**To get started, simply describe how you're feeling.**\n\n"
        "*Example:* `I have a fever and sore throat for the past 2 days.`"
    )
}
       ]   # -----------------------------
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

        warning_message = (
            "🚨 **Possible Medical Emergency Detected**\n\n"
            "Your symptoms may require immediate medical attention.\n\n"
            "Please contact your local emergency services or visit the nearest hospital immediately.\n\n"
            "⚠️ This AI assistant cannot evaluate emergency situations."
        )

        with st.chat_message("assistant"):
            st.error("🚨 Possible Medical Emergency Detected")

            st.warning(
                "Please seek immediate medical attention or contact emergency services.")


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

        with st.spinner("🩺 Reviewing your health information..."):

            try:

                answer = get_response(conversation)

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

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🩺 AI Symptom Checker")

    st.success("🟢 System Status: Online")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
✅ Symptom Analysis

✅ Emergency Detection

✅ Follow-up Questions

✅ Patient Memory
""")

    st.markdown("---")

    st.subheader("⚠ Disclaimer")

    st.info(
        """
This chatbot provides **educational healthcare information only**.

It **does not diagnose diseases** or replace professional medical advice.

If you are experiencing severe symptoms,
please contact emergency medical services.
"""
    )

    st.markdown("---")

    if st.button("🗑 Clear Conversation", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 **Welcome to the AI Symptom Checking Chatbot!**\n\n"
                    "Describe your symptoms to begin."
                )
            }
        ]

        st.rerun()
        st.markdown("---")

st.caption(
    "🩺 AI Symptom Checking Chatbot | Built with Streamlit & Google Gemini | Version 1.0"
)