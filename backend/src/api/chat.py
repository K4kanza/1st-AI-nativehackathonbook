import logging
from fastapi import APIRouter, HTTPException
from uuid import UUID
from src.services.agent_service import agent_service
from src.services.chat_history_service import chat_history_service
from src.models.schemas import ChatRequest, ChatResponse, ChatMessageSchema
import json

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    user_id = "test_user"

    # -----------------------------
    # Retrieve or create session
    # -----------------------------
    try:
        if request.session_id:
            try:
                session_uuid = UUID(request.session_id)
                session = await chat_history_service.get_session_by_id(session_uuid)
                if not session:
                    session = await chat_history_service.create_session(user_id)
            except ValueError:
                session = await chat_history_service.create_session(user_id)
        else:
            session = await chat_history_service.create_session(user_id)
    except Exception as e:
        logger.error(f"Error creating/retrieving session: {e}")
        raise HTTPException(status_code=500, detail="Failed to create or retrieve chat session")

    # -----------------------------
    # Save user message
    # -----------------------------
    try:
        await chat_history_service.save_message(
            session_id=session.id,
            role="user",
            content=request.message
        )
    except Exception as e:
        logger.error(f"Failed to save user message: {e}")
        raise HTTPException(status_code=500, detail="Failed to save user message")

    # -----------------------------
    # Get AI response
    # -----------------------------
    try:
        response_content = await agent_service.get_response(
            user_message=request.message
        )
    except Exception as e:
        logger.error(f"Failed to get AI response: {e}")
        raise HTTPException(status_code=500, detail="Failed to get AI response")

    # -----------------------------
    # Save assistant message
    # -----------------------------
    try:
        await chat_history_service.save_message(
            session_id=session.id,
            role="assistant",
            content=response_content
        )
    except Exception as e:
        logger.error(f"Failed to save assistant message: {e}")
        raise HTTPException(status_code=500, detail="Failed to save assistant message")

    # -----------------------------
    # Return full history
    # -----------------------------
    full_history_orm = await chat_history_service.get_history(session.id)
    full_history_schema = [
        ChatMessageSchema.model_validate({
            "id": str(msg.id),
            "session_id": str(msg.session_id),
            "role": msg.role,
            "content": msg.content,
            "context_text": msg.context_text,
            "metadata_": json.loads(msg.metadata_) if msg.metadata_ else None,
            "created_at": msg.created_at,
        })
        for msg in full_history_orm
    ]

    return ChatResponse(
        session_id=str(session.id),
        response=response_content,
        history=full_history_schema
    )
