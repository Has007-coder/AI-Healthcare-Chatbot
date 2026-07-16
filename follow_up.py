def generate_follow_up_questions(symptom_data):

    questions = []

    if not symptom_data.get("duration"):
        questions.append(
            "How long have you been experiencing these symptoms?"
        )

    if not symptom_data.get("severity"):
        questions.append(
            "How severe are your symptoms (mild, moderate, or severe)?"
        )

    if not symptom_data.get("age"):
        questions.append(
            "Could you tell me your age?"
        )

    if not symptom_data.get("symptoms"):
        questions.append(
            "Could you describe your symptoms in more detail?"
        )

    return questions