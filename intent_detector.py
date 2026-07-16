def detect_intent(message):
    """
    Detect the user's intent based on their message.
    """

    text = message.lower().strip()

    # Greetings
    greetings = [
        "hi", "hello", "hey", "good morning",
        "good afternoon", "good evening"
    ]

    # Gratitude
    thanks = [
        "thank you", "thanks", "thankyou", "thx"
    ]

    # Goodbye
    goodbye = [
        "bye", "goodbye", "see you", "take care"
    ]

    # General health questions
    health_keywords = [
        "what is",
        "what causes",
        "how to",
        "prevent",
        "treatment",
        "medicine",
        "symptoms of"
    ]

    if any(word == text for word in greetings):
        return "greeting"

    if any(word == text for word in thanks):
        return "thanks"

    if any(word == text for word in goodbye):
        return "goodbye"

    if any(keyword in text for keyword in health_keywords):
        return "health_question"

    return "symptom"