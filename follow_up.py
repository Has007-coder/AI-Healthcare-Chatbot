"""
Generates follow-up questions based on missing patient information.
"""


def generate_follow_up_questions(missing_field):
    """
    Returns a follow-up question for the missing field.
    """

    questions = {
        "symptoms": (
            "Could you please describe your symptoms in more detail?"
        ),

        "duration": (
            "How long have you been experiencing these symptoms?"
        ),

        "severity": (
            "How severe are your symptoms? (Mild, Moderate, or Severe)"
        ),

        "age": (
            "May I know your age?"
        ),

        "gender": (
            "What is your gender?"
        )
    }

    return questions.get(
        missing_field,
        "Could you provide more information?"
    )