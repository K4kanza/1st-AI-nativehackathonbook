# Research: RAG Chatbot for Book

**Feature**: RAG Chatbot for Book
**Date**: 2025-12-28
**Branch**: `002-rag-chatbot-book`

## Technology Decisions

### Backend Framework: Python + FastAPI

**Decision**: Use Python 3.11+ with FastAPI for the backend service.

**Rationale**:
- Native async/await support ideal for I/O-bound operations (Qdrant queries, Gemini API calls)
- Extensive ecosystem for RAG and embeddings (sentence-transformers, LangChain integrations)
- FastAPI provides automatic OpenAPI documentation and type validation
- Google GenerativeAI SDK has first-class Python support

**Alternatives Considered**:
- Node.js/Express: Good async support, but RAG ecosystem less mature in JS
- Go/Gin: High performance, but less convenient for LLM integrations

### LLM Integration: Google GenerativeAI SDK

**Decision**: Use Google GenerativeAI SDK for Gemini model access.

**Rationale**:
- Official unified SDK supporting all Gemini models
- Built-in support for streaming responses
- Simple API for generateContent and streamGenerateContent
- No API key exposure risk when used server-side

**Alternatives Considered**:
- Direct HTTP calls: More error-prone, manual token management
- LangChain abstraction: Adds unnecessary dependency for simple use case

### Vector Database: Qdrant Cloud

**Decision**: Use Qdrant Cloud free tier for vector storage.

**Rationale**:
- Python-first client library
- Free tier supports ~1M vectors of 768 dimensions (sufficient for textbook)
- Efficient filtering by payload fields (book_version, chapter, anchor)
- Rust-based core for high performance

**Alternatives Considered**:
- Pinecone: More expensive, less flexible filtering
- Weaviate: Good but more complex setup
- pgvector: Would require additional Postgres load; Neon handles this separately

### Database: Neon Postgres with Pooling

**Decision**: Use Neon serverless Postgres with connection pooling (PgBouncer).

**Rationale**:
- Serverless-friendly connection handling
- PgBouncer pooling prevents connection exhaustion under high concurrency
- Native support for asyncpg async driver
- Git SHA tracking integrates naturally with Neon

**Alternatives Considered**:
- Supabase: Good alternative, but Neon has better serverless story
- Railway Postgres: Connection limits more restrictive

### Chunking Strategy: Semantic Chapter-Section-Paragraph

**Decision**: Chunk by chapter → section → paragraph with 10-15% overlap.

**Rationale**:
- Preserves semantic coherence within chunks
- Hierarchical IDs enable filtering and citation
- Overlap prevents information loss at chunk boundaries
- Deterministic IDs (v{version}:ch{idx}:sec{idx}:p{idx}) ensure reproducibility

**Alternatives Considered**:
- Fixed-token chunks: May break mid-sentence, lose context
- Sentence-based: Too granular, poor retrieval quality
- Semantic sentence transformers: Overkill for textbook structure

### Frontend: React Chat Widget

**Decision**: Implement as a React component embedded in Docusaurus.

**Rationale**:
- Docusaurus is React-based, native component integration
- Site-wide widget via layout hook
- Per-page context automatically available via Docusaurus router
- Browser Selection API for text highlighting

**Alternatives Considered**:
- Vanilla JS: More portable but harder to maintain
- Web Components: Good isolation but less Docusaurus integration

## Integration Patterns

### Query Flow (BOOK Mode)

```
User Query → FastAPI /rag/query
            → Normalize query
            → Embed query (Gemini embeddings or sentence-transformers)
            → Qdrant top-k search (k=8-12)
            → Filter by book_version
            → Optional chapter_id bias
            → Assemble context with citation headers
            → Gemini generateContent with system prompt
            → Validate citations present
            → Return {answer, citations, chunk_ids, book_version}
```

### Selected Text Mode Flow

```
User Selection → Frontend captures selected_text + page_url + anchor
               → POST /rag/query (mode="selected_text", selected_text=...)
               → Skip retrieval, use selected_text as context
               → Gemini generateContent with strict prompt
               → If answer not in selection → "Not found in selected text"
               → Return {answer, citations=[], mode="selected_text"}
```

## Security Considerations

1. **API Key Protection**: Gemini API key never exposed to clients; only server-side usage
2. **Rate Limiting**: Per-IP and per-session limits to prevent abuse
3. **Input Sanitization**: Validate and sanitize all user inputs (question, selected_text)
4. **CORS**: Restrict to Docusaurus domain only
5. **Logging**: Query logs stored in Neon for auditability (no PII retention)

## Performance Optimization

1. **Connection Pooling**: Neon PgBouncer handles connection limits
2. **Embedding Caching**: Cache query embeddings for repeated questions
3. **Streaming Responses**: Use streamGenerateContent for better perceived latency
4. **Qdrant Optimization**: Use correct index parameters for free tier
5. **Async Throughout**: Non-blocking I/O for all external calls

## Reproducibility Requirements

1. **Deterministic Chunking**: Same book version produces identical chunk IDs
2. **Version Tracking**: Git SHA stored in Neon for every ingestion run
3. **Retrieval Logging**: All queries logged with retrieved chunk IDs
4. **Audit Trail**: Selection records linked to query logs

## Open Questions Resolved

| Question | Resolution |
|----------|------------|
| Embedding model? | Use Gemini embedding-001 or sentence-transformers/all-MiniLM-L6-v2 |
| Chunk size? | 300-800 tokens with 10-15% overlap |
| Top-k value? | Start with k=8, adjust based on evaluation |
| Streaming? | Yes, use streamGenerateContent for UX |
| Evaluation set size? | 30-50 Q/A pairs for BOOK, 10+ for SELECTED_TEXT |
