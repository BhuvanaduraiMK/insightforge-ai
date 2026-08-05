import os
import time


from app.services.conversation_service import (
    add_message,
    get_history
)
#import google.generativeai as genai
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
    )

MODEL_NAME = "models/gemini-3-flash-preview"

def ask_gemini(context: str, question: str):
    """
    Send a prompt to Gemini and return the response.
    """

     # Save user's question
    add_message("user", question)

    # Build conversation history
    history_messages = get_history()[-10:]

    history = ""

    for message in history_messages:
        history += f"{message['role'].capitalize()}: {message['content']}\n"

    prompt = f"""
You are a Senior Business Analyst.

Your responsibilities are:

• Analyze business datasets.
• Answer ONLY using the provided dataset.
• Never invent information.
• If information is unavailable, clearly state that it is not present in the dataset.
• Write professional business reports.
• Explain findings in simple business language.
• Follow the user's requested response style exactly.

Response Rules:

1. Use the dataset context as the source of truth.
2. Use conversation history only to understand the user's previous questions and references.
3. Never make assumptions or invent facts.
4. If the answer is not available in the dataset, say:
   "The uploaded dataset does not contain enough information."
5. Follow the user's requested format exactly:
   - One line → one line only.
   - Two sentences → exactly two sentences.
   - Bullet points → use bullet points.
   - Table → return a table.
   - Detailed report → include headings and explanations.
   - Executive summary → concise business summary.
6. Only provide Business Recommendations if:
   - the user explicitly asks for recommendations, OR
   - the user asks for analysis, report, business summary, or detailed explanation.
7. If the current question refers to previous questions using words like:
   - it
   - this
   - that
   - these
   - those
   - they
   - them
   then use the conversation history to understand the reference.
8. If the conversation history does not contain enough information, politely ask the user to clarify.

Formatting Rules:

• Use Markdown headings (#, ##) only for detailed reports.
• For short answers, return plain text only.
• Use bullet points only when appropriate.
• Keep answers concise unless the user asks for details.

Dataset Context:

{context}

Conversation History:

{history}

Current Question:

{question}
"""

    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            answer = response.text

            add_message("assistant", answer)

            return {
                "success": True,
                "answer": answer
            }

        except Exception as e:

            error = str(e)
            print(f"Gemini Error (Attempt {attempt+1}/3): {error}")

            if "503" in error and attempt < 2:
                time.sleep(2)
                continue

            if "429" in error:
                return {
                    "success": False,
                    "error": {
                        "type": "quota_exceeded",
                        "message": "Gemini quota exceeded. Please try again later."
                    }
                }

            if "503" in error:
                return {
                    "success": False,
                    "error": {
                        "type": "service_busy",
                        "message": "Gemini service is temporarily busy."
                    }
                }

            
            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": error
                }
            }