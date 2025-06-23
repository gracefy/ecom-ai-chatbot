# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import chat_api

app = FastAPI()

# Allow cross-origin requests from any origin (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_api.router, prefix="/chat")


@app.get("/")
async def root():
    return {
        "message": "E-Commerce AI Chatbot API is running. See /docs for API documentation."
    }
