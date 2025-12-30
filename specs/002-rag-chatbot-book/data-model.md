# Data Model: RAG Chatbot for Book

**Feature**: RAG Chatbot for Book
**Date**: 2025-12-28
**Branch**: `002-rag-chatbot-book`

## Entity Relationship Overview

```
BookVersion 1───* Chunk
BookVersion 1───* IngestRun
Session 1───* QueryLog
Session 1───* SelectionRecord
```

## Core Tables

### book_versions

Stores book version metadata for reproducibility.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment identifier |
| git_sha | VARCHAR(40) | UNIQUE NOT NULL | Git commit SHA or semantic version |
| created_at | TIMESTAMPTZ | DEFAULT NOW() | When version was recorded |
| content_path | TEXT | NOT NULL | Path to source Markdown/MDX files |
| chunk_count | INTEGER | DEFAULT 0 | Number of chunks in this version |

### chunks

Stores book content chunks with embeddings.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| chunk_id | TEXT | PRIMARY KEY | Deterministic ID (v{ver}:ch{idx}:sec{idx}:p{idx}) |
| book_version_id | INTEGER | FOREIGN KEY → book_versions.id | Reference to book version |
| chapter_idx | INTEGER | NOT NULL | Chapter number |
| chapter_title | TEXT | NOT NULL | Chapter title |
| section_idx | INTEGER | NOT NULL | Section number within chapter |
| section_anchor | TEXT | | URL-friendly anchor slug |
| para_idx | INTEGER | NOT NULL | Paragraph index within section |
| source_path | TEXT | NOT NULL | Path to source file |
| content_text | TEXT | NOT NULL | Chunk text content |
| text_hash | VARCHAR(64) | UNIQUE NOT NULL | SHA-256 hash of content for deduplication |
| embedding_vector | VECTOR(768) | | Gemini or sentence-transformers embedding |
| created_at | TIMESTAMPTZ | DEFAULT NOW() | When chunk was created |

**Indexes**:
- `idx_chunks_book_version` on (book_version_id)
- `idx_chunks_chapter` on (book_version_id, chapter_idx)
- `idx_chunks_text_hash` on (text_hash)
- GIN index on embedding_vector for vector similarity search

### ingest_runs

Tracks content ingestion execution for debugging.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment identifier |
| book_version_id | INTEGER | FOREIGN KEY → book_versions.id | Version being ingested |
| status | VARCHAR(20) | CHECK (IN ('running', 'completed', 'failed')) | Run status |
| started_at | TIMESTAMPTZ | DEFAULT NOW() | When ingestion started |
| finished_at | TIMESTAMPTZ | | When ingestion completed |
| total_chunks | INTEGER | DEFAULT 0 | Total chunks processed |
| failed_chunks | INTEGER | DEFAULT 0 | Chunks that failed embedding |
| metrics_json | JSONB | | Additional metrics (timing, sizes) |
| error_message | TEXT | | Error if status='failed' |

### sessions

Manages user chat sessions for continuity.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY DEFAULT gen_random_uuid() | Session identifier |
| created_at | TIMESTAMPTZ | DEFAULT NOW() | When session created |
| last_seen_at | TIMESTAMPTZ | DEFAULT NOW() | Last activity timestamp |
| user_agent | TEXT | | Browser/client user agent |
| page_url | TEXT | | Current page context |

### query_logs

Audit trail for all queries (read-only, append-only).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment identifier |
| session_id | UUID | FOREIGN KEY → sessions.id | Associated session |
| mode | VARCHAR(20) | CHECK (IN ('book', 'selected_text')) | Query mode |
| question | TEXT | NOT NULL | User's question |
| retrieved_chunk_ids | TEXT[] | | Array of chunk IDs retrieved |
| selected_text_hash | VARCHAR(64) | | Hash of selected text if mode='selected_text' |
| response_text | TEXT | | Bot's response |
| citations | TEXT[] | | Chunk IDs cited in response |
| latency_ms | INTEGER | | Total response time |
| gemini_model | VARCHAR(50) | | Model used for generation |
| created_at | TIMESTAMPTZ | DEFAULT NOW() | When query executed |

**Indexes**:
- `idx_query_logs_session` on (session_id)
- `idx_query_logs_created` on (created_at DESC)
- `idx_query_logs_mode` on (mode)

### selection_records

Tracks selected text usage for Selected Text Only mode.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment identifier |
| session_id | UUID | FOREIGN KEY → sessions.id | Associated session |
| page_url | TEXT | NOT NULL | Page where selection occurred |
| selection_text_hash | VARCHAR(64) | NOT NULL | Hash of selected text |
| selection_offsets | JSONB | | Start/end offsets in page |
| selection_context | TEXT | | Surrounding context for reference |
| created_at | TIMESTAMPTZ | DEFAULT NOW() | When selection captured |

## Pydantic Models (API Layer)

### Request Models

```python
class ChatSessionCreate(BaseModel):
    page_url: str
    user_agent: Optional[str] = None

class RAGQueryRequest(BaseModel):
    question: str
    mode: Literal["book", "selected_text"]
    page_url: str
    chapter_id: Optional[int] = None
    section_anchor: Optional[str] = None
    selected_text: Optional[str] = None

class IngestRequest(BaseModel):
    book_version: str
    content_path: str
```

### Response Models

```python
class ChunkCitation(BaseModel):
    chunk_id: str
    chapter_title: str
    section_anchor: str
    source_path: str

class RAGQueryResponse(BaseModel):
    answer: str
    citations: list[ChunkCitation]
    mode: Literal["book", "selected_text"]
    retrieved_chunk_ids: list[str]
    book_version: str
    latency_ms: int

class HealthResponse(BaseModel):
    status: str
    gemini: bool
    qdrant: bool
    neon: bool
    version: str
```

## Validation Rules

1. **Chunk ID Format**: Must match pattern `v{version}:ch{chapter}:sec{section}:p{paragraph}`
2. **Text Hash**: SHA-256 hex string (64 characters)
3. **Mode**: Must be either "book" or "selected_text"
4. **Question Length**: Maximum 2000 characters
5. **Selected Text Length**: Maximum 5000 characters
6. **Session Timeout**: Sessions auto-expire after 24 hours of inactivity
7. **Query Rate Limit**: Maximum 60 queries per minute per IP

## Migration Strategy

```sql
-- Initial schema creation (run on Neon)
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enums
CREATE TYPE ingest_status AS ENUM ('running', 'completed', 'failed');
CREATE TYPE query_mode AS ENUM ('book', 'selected_text');

-- Create tables (in order due to FK constraints)
CREATE TABLE book_versions (...);
CREATE TABLE chunks (...);
CREATE TABLE ingest_runs (...);
CREATE TABLE sessions (...);
CREATE TABLE query_logs (...);
CREATE TABLE selection_records (...);

-- Create indexes
CREATE INDEX idx_chunks_book_version ON chunks(book_version_id);
CREATE INDEX idx_chunks_embedding ON chunks USING GIN (embedding_vector vector_cosine_ops);
-- ... additional indexes
```
