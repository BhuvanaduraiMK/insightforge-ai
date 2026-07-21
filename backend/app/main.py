from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="AI-Powered Business Intelligence Platform"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}"
    }