# emergency.py

EMERGENCY_KEYWORDS = [
    "chest pain",
    "difficulty breathing",
    "can't breathe",
    "cannot breathe",
    "shortness of breath",
    "stroke",
    "heart attack",
    "seizure",
    "unconscious",
    "fainted",
    "heavy bleeding",
    "severe bleeding",
    "vomiting blood",
    "coughing blood",
    "loss of consciousness"
]


def is_emergency(user_message):
    """
    Returns True if the user's message contains
    emergency-related keywords.
    """

    message = user_message.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in message:
            return True

    return False