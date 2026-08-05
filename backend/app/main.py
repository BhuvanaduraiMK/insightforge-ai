from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="AI-Powered Business Intelligence Platform"
)

# Register API Routers
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}"
    }