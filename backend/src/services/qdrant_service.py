import cohere
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from src.core.config import settings

class QdrantService:
    def __init__(self, collection_name: str = "ai-robotics-book"):
        self.collection_name = collection_name

        # Cohere client for embeddings
        self.cohere_client = cohere.Client(settings.cohere_api_key)
        self.embed_model = "embed-english-v3.0"

        # Qdrant client
        self.client = QdrantClient(
            url=settings.qdrant_host,     # e.g., "https://your-qdrant-host"
            api_key=settings.qdrant_api_key
        )

    def create_collection(self):
        print("\nCreating Qdrant collection...")
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=1024,
                distance=Distance.COSINE
            )
        )

    def embed_text(self, text: str) -> list:
        """
        Generate embedding for a single text chunk using Cohere.
        """
        response = self.cohere_client.embed(
            model=self.embed_model,
            input_type="search_query",
            texts=[text]
        )
        return response.embeddings[0]

    def upsert_chunk(self, chunk: str, chunk_id: int, url: str):
        """
        Store a single chunk in Qdrant with embedding and metadata.
        """
        vector = self.embed_text(chunk)
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=chunk_id,
                    vector=vector,
                    payload={
                        "url": url,
                        "text": chunk,
                        "chunk_id": chunk_id
                    }
                )
            ]
        )

# Singleton instance
qdrant_service = QdrantService()
