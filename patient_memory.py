# Stores information collected during the conversation

patient_memory = {
    "symptoms": [],
    "duration": None,
    "severity": None,
    "age": None,
    "gender": None
}


def get_memory():
    """Return the current patient information."""
    return patient_memory


def update_memory(new_data):
    """
    Update memory with newly extracted information.
    Only overwrite fields if new information is available.
    """

    if new_data.get("symptoms"):
        for symptom in new_data["symptoms"]:
            if symptom not in patient_memory["symptoms"]:
                patient_memory["symptoms"].append(symptom)

    for key in ["duration", "severity", "age", "gender"]:
        value = new_data.get(key)

        if value not in [None, "", "Unknown"]:
            patient_memory[key] = value


def clear_memory():
    """Reset memory for a new conversation."""

    patient_memory["symptoms"] = []
    patient_memory["duration"] = None
    patient_memory["severity"] = None
    patient_memory["age"] = None
    patient_memory["gender"] = None