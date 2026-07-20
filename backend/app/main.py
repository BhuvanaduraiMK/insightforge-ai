print("=== main.py is executing ===")

from fastapi import FastAPI

print("=== FastAPI imported ===")

app = FastAPI()

print("=== app created ===")

@app.get("/")
def root():
    return {"message": "Welcome to InsightForge AI"}