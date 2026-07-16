def get_missing_information(symptom_analysis):
    missing = []

    if not symptom_analysis["symptoms"]:
        missing.append("symptoms")

    if not symptom_analysis["duration"]:
        missing.append("duration")

    if not symptom_analysis["severity"]:
        missing.append("severity")

    return missing