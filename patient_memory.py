"""
Stores patient information collected during the conversation.
"""

patient_memory = {
    "symptoms": [],
    "duration": None,
    "severity": None,
    "age": None,
    "gender": None
}


def get_memory():
    """Return the current patient memory."""
    return patient_memory


def update_memory(new_data):
    """
    Update patient memory with a dictionary.
    Example:
    update_memory({"age": "18"})
    update_memory({"symptoms": ["fever"]})
    """

    if not isinstance(new_data, dict):
        return

    # Update symptoms
    if "symptoms" in new_data:
        symptoms = new_data["symptoms"]

        if isinstance(symptoms, list):
            for symptom in symptoms:
                if symptom not in patient_memory["symptoms"]:
                    patient_memory["symptoms"].append(symptom)

        elif isinstance(symptoms, str):
            if symptoms not in patient_memory["symptoms"]:
                patient_memory["symptoms"].append(symptoms)

    # Update remaining fields
    for field in ["duration", "severity", "age", "gender"]:

        if field in new_data:

            value = new_data[field]

            if value not in [None, "", "Unknown"]:
                patient_memory[field] = value


def clear_memory():
    """Reset patient memory."""

    patient_memory["symptoms"] = []
    patient_memory["duration"] = None
    patient_memory["severity"] = None
    patient_memory["age"] = None
    patient_memory["gender"] = None