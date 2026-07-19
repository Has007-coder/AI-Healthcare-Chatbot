"""
Emergency symptom detection.
"""

EMERGENCY_KEYWORDS = [
    "chest pain",
    "difficulty breathing",
    "can't breathe",
    "cannot breathe",
    "heart attack",
    "stroke",
    "seizure",
    "unconscious",
    "heavy bleeding",
    "vomiting blood",
    "coughing blood",
    "loss of consciousness"
]


def is_emergency(message):
    """
    Returns True if the message contains emergency symptoms.
    """

    text = message.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text:
            return True

    return False