import logging
import asyncio
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, function_tool
from src.services.qdrant_service import qdrant_service
from src.core.config import settings
import cohere


logger = logging.getLogger(__name__)

# ------------------------
# Initialize Cohere client for embeddings
# ------------------------
cohere_client = cohere.Client(settings.cohere_api_key)

# ------------------------
# Gemini API client
# ------------------------
external_client = AsyncOpenAI(
    api_key=settings.gemini_api_key,
    base_url=settings.gemini_base_url
)

# ------------------------
# Chat model for the agent
# ------------------------
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# ------------------------
# Qdrant Retrieval Tool
# ------------------------
@function_tool
async def retrieve_from_qdrant(query: str) -> str:
    try:
        embeddings = cohere_client.embed(
            texts=[query],
            model="embed-english-v3.0",
            input_type="search_query"
        ).embeddings
        query_vector = embeddings[0]

        # Sync function to run in thread
        def _query():
            return qdrant_service.client.query_points(
                collection_name="ai-robotics-book",
                query=query_vector,
                limit=5
            )

        results = await asyncio.to_thread(_query)

        if not results or not hasattr(results, "points"):
            return "No relevant context found in the book."

        texts = [point.payload.get("text", "") for point in results.points if "text" in point.payload]
        return "\n".join(texts) if texts else "No relevant context found in the book."

    except Exception as e:
        logger.error(f"Error retrieving from Qdrant: {e}", exc_info=True)
        return "Error retrieving context from the book."

# ------------------------
# Define the Agent
# ------------------------
book_agent = Agent(
    name="Humanoid Robotics Assistant",
    instructions="""
You are  assistant for the book 'Physical AI & Humanoid Robotics'.

If the user greets or the conversation starts:
- Respond with a short friendly greeting.
- Invite the user to ask about the book.

For all book-related questions:
- Always use the Qdrant retrieval tool.
- If the answer is not found in the context, say you cannot answer.
""",
    tools=[retrieve_from_qdrant],
)


# ------------------------
# AgentService
# ------------------------
class AgentService:
    def __init__(self):
        self.agent = book_agent
        self.run_config = config

    async def get_response(self, user_message: str) -> str:
        if not user_message.strip():
            return "👋 Hello! I’m your Reg Agent Assistant. Ask me anything from the book."

    # Normal flow without selected text
        result = await Runner.run(
            starting_agent=self.agent,
            input=user_message,
            run_config=self.run_config
        )

        return result.final_output

# Initialize service
agent_service = AgentService()
