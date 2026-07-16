# 🩺 AI Healthcare Chatbot

An AI-powered healthcare chatbot built using **Python** and the **Google Gemini API**. The chatbot provides educational health information, asks follow-up questions based on symptoms, and detects emergency situations to encourage users to seek immediate medical attention when necessary.

> ⚠️ Disclaimer: This chatbot is for educational purposes only. It does not provide medical diagnoses or replace professional healthcare advice.

---

## 🚀 Features

- 🤖 AI-powered conversations using Google Gemini
- 🩺 Symptom analysis
- ❓ Intelligent follow-up questions
- 🚨 Emergency symptom detection
- 💬 Interactive command-line interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Technologies Used

- Python 3
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
healthcare/
│
├── app.py
├── chatbot.py
├── symptom_checker.py
├── intent_detector.py
├── follow_up.py
├── emergency.py
├── prompts.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── scripts/
│   ├── api_test.py
│   ├── gemini_api_test.py
│   └── check_models.py
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project

```bash
cd healthcare
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and add your Gemini API key

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Chatbot

```bash
python app.py
```

---

## 📌 Future Improvements

- Streamlit web interface
- Conversation history
- User authentication
- Voice input/output
- Medical knowledge base integration
- Multi-language support

---

## 📄 License

This project is intended for educational purposes.