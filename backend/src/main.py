import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services.chat_history_service import chat_history_service
from src.api import chat

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="RAG Chatbot API", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "RAG Chatbot API is start!"}

@app.on_event("startup")
async def startup():
    logger.info("Starting up and initializing database...")
    await chat_history_service.initialize_database()
