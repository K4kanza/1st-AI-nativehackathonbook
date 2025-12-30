import pytest
import asyncio
from uuid import UUID
from backend.src.services.chat_history_service import chat_history_service
from backend.src.models.database import AsyncSessionLocal, Base, ChatSession, ChatMessage, async_engine

# Setup and Teardown for tests
@pytest.fixture(scope="module")
async def setup_database():
    # Create tables
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Drop tables after tests
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_session(setup_database):
    user_id = "test_user_1"
    session = await chat_history_service.create_session(user_id=user_id, metadata={"source": "test"})
    assert session is not None
    assert isinstance(session.id, UUID)
    assert session.user_id == user_id
    assert session.metadata_ == {"source": "test"}

@pytest.mark.asyncio
async def test_save_message(setup_database):
    user_id = "test_user_2"
    session = await chat_history_service.create_session(user_id=user_id)
    assert session is not None

    message_content = "Hello, AI!"
    message = await chat_history_service.save_message(
        session_id=session.id,
        role="user",
        content=message_content,
        context_text="Some selected text",
        metadata={"sentiment": "positive"}
    )
    assert message is not None
    assert isinstance(message.id, UUID)
    assert message.session_id == session.id
    assert message.role == "user"
    assert message.content == message_content
    assert message.context_text == "Some selected text"
    assert message.metadata_ == {"sentiment": "positive"}

@pytest.mark.asyncio
async def test_get_history(setup_database):
    user_id = "test_user_3"
    session = await chat_history_service.create_session(user_id=user_id)
    assert session is not None

    # Save multiple messages
    await chat_history_service.save_message(session_id=session.id, role="user", content="Msg 1")
    await asyncio.sleep(0.01) # Ensure different created_at timestamps
    await chat_history_service.save_message(session_id=session.id, role="assistant", content="Resp 1")
    await asyncio.sleep(0.01)
    await chat_history_service.save_message(session_id=session.id, role="user", content="Msg 2")

    history = await chat_history_service.get_history(session.id)
    assert len(history) == 3
    assert history[0].content == "Msg 1"
    assert history[1].content == "Resp 1"
    assert history[2].content == "Msg 2"
    assert history[0].role == "user"
    assert history[1].role == "assistant"
    assert history[2].role == "user"

@pytest.mark.asyncio
async def test_get_session_by_user_id(setup_database):
    user_id = "test_user_4"
    session1 = await chat_history_service.create_session(user_id=user_id, metadata={"version": 1})
    await asyncio.sleep(0.01)
    session2 = await chat_history_service.create_session(user_id=user_id, metadata={"version": 2})

    retrieved_session = await chat_history_service.get_session_by_user_id(user_id)
    assert retrieved_session is not None
    assert retrieved_session.id == session2.id # Should get the most recent one

@pytest.mark.asyncio
async def test_get_session_by_id(setup_database):
    user_id = "test_user_5"
    session = await chat_history_service.create_session(user_id=user_id)
    assert session is not None

    retrieved_session = await chat_history_service.get_session_by_id(session.id)
    assert retrieved_session is not None
    assert retrieved_session.id == session.id

@pytest.mark.asyncio
async def test_get_contextual_history(setup_database):
    user_id = "test_user_6"
    session = await chat_history_service.create_session(user_id=user_id)
    assert session is not None

    for i in range(10):
        await chat_history_service.save_message(session_id=session.id, role="user", content=f"Message {i}")
        await asyncio.sleep(0.001) # Small delay to ensure order

    # Get last 5 messages
    context_history = await chat_history_service.get_contextual_history(session.id, limit=5)
    assert len(context_history) == 5
    assert context_history[0].content == "Message 5"
    assert context_history[4].content == "Message 9"

    # Get all messages (limit = None, or large number)
    all_history = await chat_history_service.get_contextual_history(session.id, limit=20)
    assert len(all_history) == 10
