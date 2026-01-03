import cohere
from src.core.config import settings
from src.services.qdrant_service import qdrant_service

class IngestionService:
    def __init__(self):
        self.cohere_client = cohere.Client(settings.cohere_api_key)

    def ingest_book(self, file_path: str):
        """
        Ingests a book from a local file path.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        self.ingest_book_text(text)

    def ingest_book_text(self, text: str):
        """
        Ingests raw text directly (useful for live sitemap pages).
        """
        chunks = self._chunk_text(text)

        # Generate embeddings with Cohere
        embeddings = self.cohere_client.embed(
            texts=chunks,
            model="embed-english-v3.0",
            input_type="search_document"
        ).embeddings

        # Prepare points for Qdrant
        points = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            points.append(
                qdrant_service.client.http.models.PointStruct(
                    id=i,
                    vector=embedding,
                    payload={"text": chunk}
                )
            )

        # Upsert into Qdrant
        qdrant_service.upsert_vectors(points)
        print(f"✅ Ingested {len(chunks)} chunks into Qdrant.")

    def _chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 64):
        """
        Splits text into overlapping chunks.
        """
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunks.append(" ".join(words[i:i + chunk_size]))
        return chunks

# Singleton instance
ingestion_service = IngestionService()
