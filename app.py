import traceback
import streamlit as st

from chatbot import get_response
from emergency import is_emergency
from patient_memory import get_memory, clear_memory
from response_formatter import format_response
from report_generator import generate_report
from components.header import show_header
from components.sidebar import show_sidebar
from components.chat import show_chat


show_header()

show_chat()

show_sidebar()


