import streamlit as st

from patient_memory import get_memory, clear_memory
def show_sidebar():
    # -----------------------------
# Sidebar
# -----------------------------
 with st.sidebar:

    # =============================
    # App Title
    # =============================
    st.title("🩺 AI Symptom Checker")

    st.success("🟢 System Status: Online")

    st.markdown("---")

    # =============================
    # Patient Summary
    # =============================
    st.subheader("🧾 Patient Summary")

    memory = get_memory()

    with st.container(border=True):

        # Symptoms
        st.markdown("### 🤒 Symptoms")

        if memory["symptoms"]:
            for symptom in memory["symptoms"]:
                st.write(f"• {symptom}")
        else:
            st.caption("No symptoms recorded")

        st.divider()

        # Duration
        st.markdown("### 📅 Duration")

        if memory["duration"]:
            st.success(memory["duration"])
        else:
            st.info("Waiting for information")

        # Severity
        st.markdown("### 📈 Severity")

        if memory["severity"]:
            st.success(memory["severity"])
        else:
            st.info("Waiting for information")

        # Age
        st.markdown("### 🎂 Age")

        if memory["age"]:
            st.success(memory["age"])
        else:
            st.info("Waiting for information")

        # Gender
        st.markdown("### ⚧ Gender")

        if memory["gender"]:
            st.success(memory["gender"])
        else:
            st.info("Waiting for information")

    st.markdown("---")

    # =============================
    # Progress Bar
    # =============================
    completed = 0

    if memory["symptoms"]:
        completed += 1

    if memory["duration"]:
        completed += 1

    if memory["severity"]:
        completed += 1

    if memory["age"]:
        completed += 1

    if memory["gender"]:
        completed += 1

    progress = completed / 5

    st.subheader("📊 Information Collected")

    st.progress(progress)

    st.caption(f"{completed}/5 details collected")

    st.markdown("---")

    # =============================
    # Features
    # =============================
    st.subheader("✨ Features")

    st.markdown("""
✅ Symptom Analysis

✅ Follow-up Questions

✅ Emergency Detection

✅ Patient Memory
""")

    st.markdown("---")

    # =============================
    # Disclaimer
    # =============================
    st.subheader("⚠ Disclaimer")

    st.info(
        """
This chatbot provides educational healthcare information only.

It does not diagnose diseases or replace professional medical advice.

If your symptoms are severe,
please seek immediate medical care.
"""
    )

    st.markdown("---")
    st.markdown("---")

if st.button("📄 Generate Health Report", use_container_width=True):

    report =generate_report()

    st.session_state["health_report"] = report

    # =============================
    # Clear Conversation
    # =============================
    if st.button("🗑 Clear Conversation", use_container_width=True):

        clear_memory()

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

    # Footer
    st.caption(
        "🩺 AI Symptom Checking Chatbot\n"
        "Built with Streamlit & Google Gemini\n"
        "Version 1.0"
    )