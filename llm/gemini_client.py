import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API client
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-pro")  # Default fallback

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")
    
genai.configure(api_key=api_key)

# Initialize the model using the model name from .env
model = genai.GenerativeModel(model_name)

def generate_claim_summary(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
