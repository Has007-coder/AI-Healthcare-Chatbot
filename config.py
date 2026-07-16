import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini Model
MODEL_NAME = "gemini-3.1-flash-lite"