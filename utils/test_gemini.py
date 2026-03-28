import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API key found:", bool(api_key))
print("API key starts with:", api_key[:8] + "..." if api_key else "None")

genai.configure(api_key=api_key)

print("\nAvailable models with generateContent:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print("-", m.name)

model = genai.GenerativeModel("models/gemini-1.5-flash")
response = model.generate_content("Say hello in one sentence.")
print("\nResponse:")
print(response.text)