from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="InsightForge AI",
    description="AI-Powered Business Intelligence Platform",
    version="1.0.0"
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to InsightForge AI"
    }