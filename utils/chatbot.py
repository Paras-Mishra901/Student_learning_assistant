import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_chatbot_response(prompt: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "Error: GEMINI_API_KEY not found. Check your .env file."

        genai.configure(api_key=api_key)
        model_name = "models/gemini-2.5-flash"

        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()

        if hasattr(response, "candidates") and response.candidates:
            try:
                parts = response.candidates[0].content.parts
                text = "".join([p.text for p in parts if hasattr(p, "text")])
                return text.strip() if text else "No text returned by model."
            except Exception:
                pass

        return "No response generated."

    except Exception as e:
        return f"Chatbot Error: {str(e)}"