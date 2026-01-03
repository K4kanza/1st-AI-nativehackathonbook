import logging
from typing import List, Optional
from uuid import UUID
from sqlalchemy.future import select
from src.models.database import async_engine, AsyncSessionLocal, Base, ChatSession, ChatMessage

logger = logging.getLogger(__name__)

class ChatHistoryService:
    async def initialize_database(self):
        """Create tables if they do not exist."""
        try:
            async with async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logger.info("Database tables created/checked successfully.")
        except Exception:
            logger.exception("Error initializing database")
            raise

    async def create_session(self, user_id: str, metadata: Optional[dict] = None) -> ChatSession:
        try:
            async with AsyncSessionLocal() as session:
                async with session.begin():  # Handles commit/rollback automatically
                    new_session = ChatSession(user_id=user_id, metadata_=metadata)
                    session.add(new_session)
                await session.refresh(new_session)
                logger.info(f"Created new chat session: {new_session.id}")
                return new_session
        except Exception:
            logger.exception(f"Failed to create chat session for user {user_id}")
            raise RuntimeError("Failed to create chat session")

    async def save_message(
        self,
        session_id: UUID,
        role: str,
        content: str,
        context_text: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> ChatMessage:
        try:
            async with AsyncSessionLocal() as session:
                async with session.begin():
                    new_message = ChatMessage(
                        session_id=session_id,
                        role=role,
                        content=content,
                        context_text=context_text,
                        metadata_=metadata
                    )
                    session.add(new_message)
                await session.refresh(new_message)
                logger.info(f"Saved message in session {session_id}, role: {role}")
                return new_message
        except Exception:
            logger.exception(f"Failed to save message in session {session_id}")
            raise RuntimeError("Failed to save message")

    async def get_history(self, session_id: UUID) -> List[ChatMessage]:
        try:
            async with AsyncSessionLocal() as session:
                result = await session.execute(
                    select(ChatMessage)
                    .filter(ChatMessage.session_id == session_id)
                    .order_by(ChatMessage.created_at)
                )
                return result.scalars().all()
        except Exception:
            logger.exception(f"Failed to retrieve history for session {session_id}")
            return []

    async def get_session_by_id(self, session_id: UUID) -> Optional[ChatSession]:
        try:
            async with AsyncSessionLocal() as session:
                result = await session.execute(
                    select(ChatSession).filter(ChatSession.id == session_id)
                )
                return result.scalars().first()
        except Exception:
            logger.exception(f"Failed to retrieve session by ID {session_id}")
            return None

chat_history_service = ChatHistoryService()
