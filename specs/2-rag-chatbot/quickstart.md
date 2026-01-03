# Quickstart Guide: Integrated RAG Chatbot for Book

## Getting Started

This guide will help you set up the environment and begin working on the RAG chatbot project for book integration.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+ (for backend services)
- Node.js 16+ (for frontend development)
- Git (for version control)
- Docker (for local development, optional)
- Google Cloud account with Gemini API access

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd book-ai
   ```

2. **Set up backend environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up frontend environment**
   ```bash
   cd frontend
   npm install
   ```

4. **Configure environment variables**
   Create a `.env` file in the backend directory with:
   ```
   GEMINI_API_KEY=your-gemini-api-key
   QDRANT_URL=your-qdrant-cloud-url
   QDRANT_API_KEY=your-qdrant-api-key
   NEON_DATABASE_URL=your-neon-database-url
   ```

### Project Structure

The RAG chatbot project is organized as follows:

```
backend/
├── src/
│   ├── api/          # API endpoints
│   ├── models/       # Pydantic models
│   ├── services/     # Business logic
│   └── utils/        # Utility functions
├── tests/
└── requirements.txt

frontend/
├── src/
│   ├── components/   # React components
│   ├── services/     # API clients
│   └── hooks/        # Custom hooks
├── tests/
└── package.json

docusaurus/
├── src/
│   └── components/   # Docusaurus-specific components
├── static/
└── docusaurus.config.js
```

### Running the Application

1. **Start the backend service**:
   ```bash
   cd backend
   uvicorn src.main:app --reload
   ```

2. **Start the frontend development server**:
   ```bash
   cd frontend
   npm start
   ```

3. **For Docusaurus integration**:
   ```bash
   cd docusaurus
   npm start
   ```

### Key Components

#### Backend (FastAPI)
- `/api/rag/query` - Main RAG query endpoint
- `/api/rag/ingest` - Content ingestion endpoint (protected)
- `/api/chat/session` - Session management
- `/api/health` - Health check endpoint

#### Frontend (React)
- `ChatWidget` - Main chat interface component
- `SelectionHandler` - Captures highlighted text
- `Citation` - Displays citation information

#### Data Flow
1. Content is ingested and chunked into vector database
2. User asks a question through the chat widget
3. Backend retrieves relevant chunks from Qdrant
4. Gemini generates a response based on retrieved context
5. Response with citations is returned to the frontend

### Ingesting Book Content

To ingest book content into the system:

1. Prepare your book content in Markdown/MDX format
2. Call the ingestion endpoint:
   ```bash
   curl -X POST http://localhost:8000/api/rag/ingest \
        -H "Content-Type: application/json" \
        -d '{
          "source_path": "/path/to/book/content",
          "version": "v1.0.0"
        }'
   ```

### Testing

Run backend tests:
```bash
cd backend
python -m pytest
```

Run frontend tests:
```bash
cd frontend
npm test
```

### Environment Configuration

#### Google Gemini API
1. Go to Google Cloud Console
2. Enable the Generative Language API
3. Create an API key
4. Set the `GEMINI_API_KEY` environment variable

#### Qdrant Cloud
1. Sign up for Qdrant Cloud
2. Create a new cluster
3. Note the URL and API key
4. Set the `QDRANT_URL` and `QDRANT_API_KEY` environment variables

#### Neon Postgres
1. Sign up for Neon
2. Create a new project
3. Get the connection string
4. Set the `NEON_DATABASE_URL` environment variable

### Common Tasks

- **Re-ingest content**: Use the ingestion endpoint with a new version identifier
- **Check system health**: Visit `/api/health` endpoint
- **View query logs**: Check Neon database query_logs table
- **Update citations format**: Modify the citation generation logic in services

### Troubleshooting

- If Gemini API calls fail: Verify your API key and billing setup
- If Qdrant connection fails: Check your URL and API key
- If database operations fail: Verify your Neon connection string
- If chunking doesn't work: Ensure your content is in the correct format
- If frontend can't connect to backend: Check CORS settings in FastAPI