from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.storage import session_store
from app.services.gemini_service import ask_gemini


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):

    if not session_store.business_context:

        raise HTTPException(
            status_code=400,
            detail="Please upload a dataset first"
        )

    result = ask_gemini(
        session_store.business_context,
        request.question
    )

    if not result.get("success", False):

        return {
            "question": request.question,
            "success": False,
            "answer": "",
            "error": result.get(
                "error",
                {
                    "type": "unknown_error",
                    "message": "Unable to generate answer."
                }
            )
        }

    return {
        "question": request.question,
        "success": True,
        "answer": result.get("answer", "")
    }