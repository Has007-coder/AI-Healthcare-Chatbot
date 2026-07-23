import streamlit as st

def show_patient_summary(memory):

    st.markdown("<div class='summary-card'>", unsafe_allow_html=True)

    st.markdown("<h3>📋 Patient Summary</h3>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='summary-item'><strong>Symptoms:</strong> {memory.get('symptoms','Not provided')}</div>
    <div class='summary-item'><strong>Duration:</strong> {memory.get('duration','Not provided')}</div>
    <div class='summary-item'><strong>Severity:</strong> {memory.get('severity','Not provided')}</div>
    <div class='summary-item'><strong>Age:</strong> {memory.get('age','Not provided')}</div>
    <div class='summary-item'><strong>Gender:</strong> {memory.get('gender','Not provided')}</div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)