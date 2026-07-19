def format_response(ai_response: str):
    """
    Format the AI response into a professional healthcare card.
    """

    formatted = f"""
## 🩺 Health Assessment

---

### 📋 Summary

{ai_response}

---

### 💡 Remember

- Stay hydrated
- Get adequate rest
- Monitor your symptoms

---

### ⚠️ Seek Medical Care Immediately If

- Difficulty breathing
- Severe chest pain
- Loss of consciousness
- Symptoms rapidly worsen

---

### ❗ Disclaimer

This chatbot provides educational information only and is **not a substitute for professional medical advice**.
"""

    return formatted