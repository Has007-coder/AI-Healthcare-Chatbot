import streamlit as st

from components.header import show_header
from components.sidebar import show_sidebar
from pages.chat import show_chat


# -----------------------------------------
# Load CSS
# -----------------------------------------
def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -----------------------------------------
# Main App
# -----------------------------------------
def main():
    st.set_page_config(
        page_title="AI Healthcare Assistant",
        page_icon="🏥",
        layout="wide",
    )

    load_css()

    show_header()

    show_chat()

    show_sidebar()


if __name__ == "__main__":
    main()