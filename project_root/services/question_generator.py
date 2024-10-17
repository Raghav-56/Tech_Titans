import google.generativeai as genai
from config import G_API_KEY

genai.configure(api_key=G_API_KEY)
ai_model = genai.GenerativeModel("gemini-1.5-flash")


def generate_questions(text):
    """Generate questions based on the text using Gemini AI"""
    prompt = f"Based on the following text, generate 3 insightful questions:\n\n{text[:4000]}"  # Limit text to 4000 chars
    response = ai_model.generate_content(prompt)
    return response.text.split("\n")
