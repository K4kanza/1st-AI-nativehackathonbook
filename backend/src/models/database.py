from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship
import uuid

Base = declarative_base()

# Async engine for Neon/Postgres
async_engine = create_async_engine(
    "postgresql+asyncpg://neondb_owner:npg_6WbRgdAO9slD@ep-steep-grass-a4i928yh-pooler.us-east-1.aws.neon.tech/neondb",
    echo=True,
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class ChatSession(Base):
    __tablename__ = "chat_sessions"
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())
    metadata_ = Column(String, nullable=True)

    messages = relationship("ChatMessage", back_populates="session")


class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(PG_UUID(as_uuid=True), ForeignKey("chat_sessions.id"))
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)
    context_text = Column(String, nullable=True)
    metadata_ = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=False), server_default=func.now())

    session = relationship("ChatSession", back_populates="messages")
