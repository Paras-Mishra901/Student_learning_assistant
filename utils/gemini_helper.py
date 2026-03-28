import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")
genai.configure(api_key=GEMINI_API_KEY, transport='rest')

model = genai.GenerativeModel('gemini-3-flash-preview')


def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)

        if response.candidates:
            return response.text.strip()
        return "No response generated (check safety settings)."
    except Exception as e:
        return f"Error: {str(e)}"