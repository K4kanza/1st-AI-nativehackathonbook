import asyncio
from src.services.chat_history_service import chat_history_service

async def main():
    print("Initializing database...")
    await chat_history_service.initialize_database()
    print("Database initialization complete.")

if __name__ == "__main__":
    asyncio.run(main())