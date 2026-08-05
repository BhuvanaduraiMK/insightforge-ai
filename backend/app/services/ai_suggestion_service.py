from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_suggestions(profile, kpis, insights):

    prompt = f"""
You are a Senior Business Analyst.

Based ONLY on the following dataset information, generate 8 useful business questions.

Rules:

- Questions must be answerable using this dataset.
- Do NOT invent columns.
- Questions should help business users analyze the data.
- Return ONLY the questions.
- One question per line.
- Do NOT number them.
- Do NOT explain anything.

Dataset Profile:

{profile}

KPIs:

{kpis}

Insights:   

{insights}
"""
    try:
        Model_Name = "models/gemini-3-flash-preview"

        response = client.models.generate_content(
            model= Model_Name,
            contents=prompt
        )

        text = response.text

        suggestions = []

        for line in text.split("\n"):
            line = line.strip()

            line = line.lstrip("-•1234567890. ")

            if line:
                suggestions.append(line)

        return suggestions[:8]

    except Exception:
        return [
        "Give me a business summary.",
        "What are the top KPIs?",
        "Which category performs best?",
        "Which segment needs improvement?",
        "Give me business recommendations."
        ]