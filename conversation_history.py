import streamlit as st
import uuid


def initialize_history():
    """Initialize conversation history."""
    if "conversations" not in st.session_state:
        first_chat = str(uuid.uuid4())

        st.session_state.conversations = {
            first_chat: {
                "title": "New Consultation",
                "messages": [],
                "memory": {}
            }
        }

        st.session_state.current_chat = first_chat


def get_current_chat():
    return st.session_state.current_chat


def get_current_conversation():
    chat_id = get_current_chat()
    return st.session_state.conversations[chat_id]


def save_messages(messages):
    chat_id = get_current_chat()
    st.session_state.conversations[chat_id]["messages"] = messages


def save_memory(memory):
    chat_id = get_current_chat()
    st.session_state.conversations[chat_id]["memory"] = memory


def create_new_chat():
    new_chat = str(uuid.uuid4())

    st.session_state.conversations[new_chat] = {
        "title": "New Consultation",
        "messages": [],
        "memory": {}
    }

    st.session_state.current_chat = new_chat


def load_chat(chat_id):
    st.session_state.current_chat = chat_id


def rename_chat(chat_id, title):
    st.session_state.conversations[chat_id]["title"] = title


def get_all_chats():
    return st.session_state.conversations