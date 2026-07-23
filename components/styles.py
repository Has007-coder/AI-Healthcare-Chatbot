from pathlib import Path
import streamlit as st

def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "style.css"

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )
    else:
        st.error(f"CSS file not found: {css_path}")