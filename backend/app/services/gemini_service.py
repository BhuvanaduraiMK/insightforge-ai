import os
import time

#import google.generativeai as genai
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
    )



def ask_gemini(context: str, question: str):
    """
    Send a prompt to Gemini and return the response.
    """

    prompt = f"""
    YYou are a Senior Business Analyst.

    Your responsibilities are:

    • Analyze business datasets.
    • Answer only using the provided dataset.
    • Never invent information.
    • If information is unavailable, clearly say it is not present.
    • Write professional reports.
    • Use headings and bullet points.
    • Explain findings in simple business language.
    • Provide actionable recommendations whenever possible.
    
    Always end your answer with

    Business Recommendations

    containing 3-5 actionable recommendations.

    Dataset Context:

    {context}

    Question:
    {question}
"""

    
    for attempt in range(3):
        try: 
            response = client.models.generate_content(
                    model = "models/gemini-3-flash-preview",
                    contents = prompt
                )
            return response.text

        except Exception as e:
            print(e)

            if attempt == 2:
                raise

            print(f"Retry {attempt+1}/3...")
            time.sleep(3)

