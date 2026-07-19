"""
Checks what patient information is still missing.
"""


def get_missing_information(memory):
    """
    Returns a list of missing patient information.
    """

    missing = []

    # Symptoms
    if not memory.get("symptoms"):
        missing.append("symptoms")

    # Duration
    if not memory.get("duration"):
        missing.append("duration")

    # Severity
    if not memory.get("severity"):
        missing.append("severity")

    # Age
    if not memory.get("age"):
        missing.append("age")

    # Gender (optional)
    if not memory.get("gender"):
        missing.append("gender")

    return missing