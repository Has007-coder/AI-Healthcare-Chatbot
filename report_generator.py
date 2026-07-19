from patient_memory import get_memory
from datetime import datetime


def generate_report():

    memory = get_memory()

    symptoms = (
        ", ".join(memory["symptoms"])
        if memory["symptoms"]
        else "Not provided"
    )

    report = f"""
# 🩺 AI Health Report

## Patient Information

**Age:** {memory["age"] or "Not provided"}

**Gender:** {memory["gender"] or "Not provided"}

## Symptoms

{symptoms}

## Duration

{memory["duration"] or "Not provided"}

## Severity

{memory["severity"] or "Not provided"}

## Generated On

{datetime.now().strftime("%d %B %Y %I:%M %p")}
"""

    print(report)   # Debug

    return report