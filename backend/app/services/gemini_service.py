import os
import time

from dotenv import load_dotenv
from google import genai

from app.services.conversation_service import (
    add_message,
    get_history
)


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL_NAME = "models/gemini-3-flash-preview"


def ask_gemini(context: str, question: str):
    """
    Send a question to Gemini using the generated
    business dataset context.
    """

    # ==========================================================
    # GET PREVIOUS CONVERSATION
    # ==========================================================

    history_messages = get_history()[-10:]

    history_lines = []

    for message in history_messages:

        role = message.get(
            "role",
            "user"
        )

        content = message.get(
            "content",
            ""
        )

        history_lines.append(
            f"{role.capitalize()}: {content}"
        )

    history = "\n".join(
        history_lines
    )

    # ==========================================================
    # PROMPT
    # ==========================================================

    prompt = f"""
You are a Senior Business Analyst working with an uploaded
business dataset.

Your job is to answer questions using ONLY the Dataset Context.

============================================================
CORE RULE
============================================================

The Dataset Context is the source of truth.

Never invent information.

Never assume information.

Never use outside knowledge to create dataset facts.

Before saying that information is unavailable, search the
ENTIRE Dataset Context carefully.

If the requested information exists anywhere in the context,
you MUST answer using that information.

Only say:

"The uploaded dataset does not contain enough information."

when the required information genuinely does not exist
in the Dataset Context.

============================================================
NUMERICAL QUESTIONS
============================================================

For questions involving:

• average
• mean
• median
• minimum
• maximum
• highest
• lowest
• count
• percentage
• churn rate
• comparison
• difference
• correlation

use the precomputed values from the Dataset Context.

Do not invent alternative values.

============================================================
GROUP QUESTIONS
============================================================

For questions such as:

"average X by Y"

"highest X among Y"

"lowest X among Y"

"how does X vary across Y"

use the corresponding:

"Average <column> by <category>"

section.

============================================================
CHURN QUESTIONS
============================================================

For churn questions use:

• Churn Analysis
• Churn Rate by Category

For questions comparing churned and active members,
use:

• Satisfaction by Churn Status

when available.

============================================================
BUSINESS RECOMMENDATIONS
============================================================

Provide recommendations ONLY when:

1. The user explicitly asks for recommendations, OR
2. The user asks for analysis, report, business summary,
   or detailed explanation.

Recommendations must be supported by numerical evidence
from the Dataset Context.

Do not create unsupported recommendations.

============================================================
CONVERSATION HISTORY
============================================================

Use conversation history ONLY to understand references such as:

• it
• this
• that
• these
• those
• they
• them
• previous result
• previous question

Do not use conversation history as a replacement for the
Dataset Context.

If the reference cannot be understood from the history,
ask the user for clarification.

============================================================
RESPONSE FORMAT
============================================================

Follow the user's requested format.

If the user asks for:

One line:
→ return one line.

Two sentences:
→ return exactly two sentences.

Bullet points:
→ use bullet points.

Table:
→ return a Markdown table.

Detailed report:
→ use Markdown headings and explanations.

Executive summary:
→ keep it concise and business-focused.

Simple question:
→ answer directly.

Do not add unnecessary explanations.

============================================================
DATASET CONTEXT
============================================================

{context}

============================================================
CONVERSATION HISTORY
============================================================

{history}

============================================================
CURRENT QUESTION
============================================================

{question}

============================================================
FINAL CHECK
============================================================

Before answering:

1. Search the Dataset Context.
2. Find the relevant section.
3. Use the exact available value.
4. Compare groups when required.
5. Do not invent information.
6. Only declare information unavailable if it is genuinely
   absent.
"""

    # ==========================================================
    # SAVE CURRENT QUESTION
    # ==========================================================

    add_message(
        "user",
        question
    )

    # ==========================================================
    # CALL GEMINI
    # ==========================================================

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            answer = (
                response.text
                if response.text
                else "Unable to generate an answer."
            )

            add_message(
                "assistant",
                answer
            )

            return {
                "success": True,
                "answer": answer
            }

        except Exception as e:

            error = str(e)

            print(
                f"Gemini Error "
                f"(Attempt {attempt + 1}/3): "
                f"{error}"
            )

            # --------------------------------------------------
            # 503 - retry
            # --------------------------------------------------

            if (
                "503" in error
                and attempt < 2
            ):

                time.sleep(2)

                continue

            # --------------------------------------------------
            # 429 - quota
            # --------------------------------------------------

            if "429" in error:

                return {
                    "success": False,
                    "error": {
                        "type": "quota_exceeded",
                        "message": (
                            "Gemini quota exceeded. "
                            "Please try again later."
                        )
                    }
                }

            # --------------------------------------------------
            # 503 - service busy
            # --------------------------------------------------

            if "503" in error:

                return {
                    "success": False,
                    "error": {
                        "type": "service_busy",
                        "message": (
                            "Gemini service is temporarily busy."
                        )
                    }
                }

            # --------------------------------------------------
            # Other errors
            # --------------------------------------------------

            return {
                "success": False,
                "error": {
                    "type": "internal_error",
                    "message": error
                }
            }

    return {
        "success": False,
        "error": {
            "type": "unknown_error",
            "message": (
                "Unable to generate AI response."
            )
        }
    }