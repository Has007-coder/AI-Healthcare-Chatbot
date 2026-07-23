import streamlit as st

def show_header():
    st.markdown("""
    <div class="hero">
        <div class="hero-icon">🩺</div>
        <div>
            <h1>AI Healthcare Assistant</h1>
            <p>Your intelligent symptom checker powered by AI</p>
        </div>
    </div>
    """, unsafe_allow_html=True)