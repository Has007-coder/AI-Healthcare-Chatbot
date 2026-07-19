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
    with st.chat_message(
    "user",
    avatar="👤"
):
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

                if "health_report" in st.session_state:


                 st.markdown("---")
                 st.subheader("📄 AI Health Report")

                 st.markdown(st.session_state["health_report"])


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

    report = generate_report()

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