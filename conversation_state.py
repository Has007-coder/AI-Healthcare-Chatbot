conversation_state = {
    "waiting_for": None
}


def set_waiting(field):
    """
    Tell the chatbot what information it expects next.
    """
    conversation_state["waiting_for"] = field


def get_waiting():
    """
    Return the field the chatbot is waiting for.
    """
    return conversation_state["waiting_for"]


def clear_waiting():
    """
    Clear the waiting state after receiving the answer.
    """
    conversation_state["waiting_for"] = None