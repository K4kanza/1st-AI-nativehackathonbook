from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ChatMessageSchema(BaseModel):
    id: str
    session_id: str
    role: str
    content: str
    created_at: datetime
    context_text: Optional[str] = None
    metadata_: Optional[dict] = None

    class Config:
        from_attributes = True # Allow ORM models to be converted to Pydantic models

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    context_mode: str = "full_book"
    selected_text: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: Optional[str] = None
    response: str
    history: List[ChatMessageSchema] = []
