import re

# Common symptoms
SYMPTOMS = [
    "fever",
    "cough",
    "cold",
    "headache",
    "sore throat",
    "vomiting",
    "nausea",
    "diarrhea",
    "stomach pain",
    "chest pain",
    "dizziness",
    "fatigue",
    "body pain",
    "back pain",
    "shortness of breath",
    "rash",
    "runny nose"
]

# Severity keywords
SEVERITY = [
    "mild",
    "moderate",
    "severe",
    "extreme",
    "worst"
]


def analyze_symptoms(text):
    """
    Analyze the user's complete conversation and
    extract structured health information.
    """

    text = text.lower()

    # Detect symptoms
    detected_symptoms = []

    for symptom in SYMPTOMS:
        if symptom in text:
            detected_symptoms.append(symptom)

    # Remove duplicate symptoms
    detected_symptoms = list(set(detected_symptoms))

    # Detect severity
    detected_severity = None

    for level in SEVERITY:
        if level in text:
            detected_severity = level
            break

    # Detect duration
    duration = None

    duration_pattern = (
        r"(\d+)\s*(day|days|week|weeks|month|months|hour|hours)"
    )

    duration_match = re.search(duration_pattern, text)

    if duration_match:
        duration = duration_match.group()

    # Detect age
    age = None

    age_match = re.search(
        r"(\d{1,3})\s*(years|year|yrs|yr|yo)",
        text
    )

    if age_match:
        age = age_match.group(1)

    # Detect gender
    gender = None

    if "male" in text:
        gender = "Male"

    elif "female" in text:
        gender = "Female"

    return {
        "symptoms": detected_symptoms,
        "severity": detected_severity,
        "duration": duration,
        "age": age,
        "gender": gender
    }

