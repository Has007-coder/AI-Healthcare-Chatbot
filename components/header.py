import streamlit as st


def show_header():

    st.title("🩺 AI Symptom Checking Chatbot")

    st.markdown("""
### Your Intelligent Healthcare Companion

Describe your symptoms, and I'll ask follow-up questions to better understand your condition and provide **educational health guidance**.

> ⚠️ **Disclaimer:** This chatbot does **not** diagnose diseases or replace professional medical advice.
""")