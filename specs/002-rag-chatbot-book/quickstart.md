# Quickstart: RAG Chatbot for Book

**Feature**: RAG Chatbot for Book
**Date**: 2025-12-28
**Branch**: `002-rag-chatbot-book`

## Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git
- API keys:
  - Google Gemini API key
  - Qdrant Cloud URL + API key
  - Neon database URL

## Environment Setup

### 1. Clone and Setup

```bash
git checkout 002-rag-chatbot-book
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

Create `.env` file in `backend/`:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_connection_string
NEON_POOL_DATABASE_URL=your_neon_pooled_connection_string

# Optional
LOG_LEVEL=INFO
RATE_LIMIT_REQUESTS_PER_MINUTE=60
CHUNK_OVERLAP=0.15
TOP_K_RETRIEVAL=8
GEMINI_MODEL=gemini-1.5-flash
```

### 3. Local Development with Docker Compose

```bash
# Start supporting services (if not using cloud instances)
docker-compose up -d qdrant postgres

# Or use all cloud services and just run the FastAPI server
uvicorn src.main:app --reload --port 8000
```

### 4. Database Setup

```bash
# Run migrations
alembic upgrade head

# Or create tables directly
python -c "from db.init import init_db; init_db()"
```

### 5. Ingest Book Content

```bash
# Ingest from local Markdown files
python -m ingest run --path ../content --version v1.0.0

# Verify ingestion
python -m ingest verify --version v1.0.0
```

### 6. Run Tests

```bash
# All tests
pytest

# Unit tests only
pytest tests/unit/

# Integration tests
pytest tests/integration/

# Contract tests (OpenAPI validation)
pytest tests/contract/
```

## Project Structure

```
backend/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # FastAPI routes
│   │   └── dependencies.py    # Shared dependencies
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py      # Neon connection management
│   │   ├── models.py          # SQLAlchemy models
│   │   └── schemas.py         # Pydantic schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini.py          # Gemini API integration
│   │   ├── qdrant.py          # Vector retrieval
│   │   ├── chunker.py         # Content chunking
│   │   └── rag.py             # RAG orchestration
│   ├── ingest/
│   │   ├── __init__.py
│   │   └── cli.py             # Ingestion CLI
│   └── main.py                # FastAPI application
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   ├── integration/
│   └── contract/
├── scripts/
│   └── setup-db.sh
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## API Usage

### Create Session

```bash
curl -X POST http://localhost:8000/v1/chat/session \
  -H "Content-Type: application/json" \
  -d '{"page_url": "https://book.example.com/chapter1"}'
```

### Query (BOOK mode)

```bash
curl -X POST http://localhost:8000/v1/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is physical AI?",
    "mode": "book",
    "page_url": "https://book.example.com/chapter1",
    "chapter_id": 2
  }'
```

### Query (SELECTED_TEXT mode)

```bash
curl -X POST http://localhost:8000/v1/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Summarize this paragraph",
    "mode": "selected_text",
    "page_url": "https://book.example.com/chapter1",
    "selected_text": "Physical AI represents..."
  }'
```

### Health Check

```bash
curl http://localhost:8000/v1/health
```

## Frontend Integration

### Docusaurus Setup

Add to `docusaurus.config.js`:

```javascript
themes: [
  [
    '@easyops-cn/docusaurus-search-local',
    {
      hashed: true,
    },
  ],
],
```

Add chat widget to `src/theme/Root.js`:

```javascript
import ChatWidget from '@site/src/components/ChatWidget';

export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection refused to Qdrant | Verify QDRANT_URL and firewall rules |
| Neon connection errors | Use pooled connection string for serverless |
| Gemini API rate limits | Implement exponential backoff |
| Empty retrieval results | Check book_version matches ingested content |
| Missing citations | Verify system prompt includes citation instructions |

## Performance Tuning

- Adjust `TOP_K_RETRIEVAL` (default: 8) based on response quality
- Enable embedding caching for repeated queries
- Use connection pooling for Neon in serverless environments
- Consider batch ingestion for large books
