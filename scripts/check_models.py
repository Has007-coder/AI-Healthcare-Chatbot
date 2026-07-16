from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

test_models = [
    "gemini-flash-latest",
    "gemini-2.0-flash",
    "gemini-2.0-flash-001",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite"
]

for model in test_models:
    try:
        response = client.models.generate_content(
            model=model,
            contents="Say hello"
        )
        print(f"✅ {model} works")
    except Exception as e:
        print(f"❌ {model}: {e}")
