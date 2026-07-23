import streamlit as st

from components.styles import load_css
from components.login_form import show_login_form


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Healthcare Chatbot",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Load CSS
# -----------------------------
load_css()

# -----------------------------
# Initialize Login State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Logo & Title
# -----------------------------
st.markdown(
    """
    <h1 class='main-title'>🩺 AI Healthcare Chatbot</h1>
    <p class='subtitle'>
        Your AI-powered Health Assistant
    </p>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Login Form
# -----------------------------
email, password, remember_me, login_clicked = show_login_form()

# -----------------------------
# Login Logic
# -----------------------------
if login_clicked:

    if email and password:

        st.session_state.logged_in = True

        st.success("✅ Login Successful!")

        st.switch_page("pages/chat.py")

    else:

        st.error("Please enter both email and password.")