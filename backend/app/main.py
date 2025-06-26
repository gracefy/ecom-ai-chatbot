# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import chat_api, product_api
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Allow cross-origin requests from any origin (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_api.router, tags=["chat"])
app.include_router(product_api.router, tags=["product"])

app.mount("/", StaticFiles(directory="static", html=True), name="static")
