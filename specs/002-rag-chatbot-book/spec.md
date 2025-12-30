# Feature Specification: RAG Chatbot for Book

**Feature Branch**: `002-rag-chatbot-book`
**Created**: 2025-12-28
**Status**: Draft
**Input**: User description: "Build a Retrieval-Augmented Generation (RAG) chatbot embedded inside a published book site (Docusaurus) that answers questions from the book's content with a 'Selected Text Only' mode."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Book Mode Query (Priority: P1)

As a reader, I want to ask questions about the book's content so that I can understand concepts without manually searching through pages.

**Why this priority**: This is the primary use case that defines the chatbot's core value proposition.

**Independent Test**: Can be fully tested by having users ask questions about book content and verifying answers include citations to specific chunks.

**Acceptance Scenarios**:

1. **Given** a user on a book page, **When** they ask "What is physical AI?", **Then** the chatbot returns an answer grounded in retrieved chunks with citations to the relevant sections.
2. **Given** a user asks a question not covered in the book, **When** the chatbot cannot find relevant chunks, **Then** it responds "Not found in the textbook" without hallucinating.
3. **Given** a user on chapter 3, **When** they ask a general question, **Then** the chatbot may bias retrieval toward chapter 3 but can still retrieve from other chapters.

---

### User Story 2 - Selected Text Only Mode (Priority: P2)

As a researcher, I want to highlight specific text and ask questions only about that passage so that I can get answers strictly grounded in my selected source.

**Why this priority**: This mode provides a unique feature that differentiates the chatbot from generic RAG systems.

**Independent Test**: Can be fully tested by highlighting a passage and asking questions that can only be answered from the highlighted text.

**Acceptance Scenarios**:

1. **Given** a user highlights a paragraph about control theory, **When** they enable "Selected Text Only" mode and ask a question, **Then** the answer is derived only from the highlighted text.
2. **Given** a user highlights text that doesn't contain the answer, **When** they ask a question, **Then** the chatbot responds "Not found in selected text."
3. **Given** a user has no text selected, **When** they try to use Selected Text Only mode, **Then** the UI prompts them to select text first.

---

### User Story 3 - Citation and Traceability (Priority: P3)

As an instructor, I want to verify that chatbot answers are traceable to specific book sections so that I can recommend it to students with confidence.

**Why this priority**: Academic credibility requires traceability to source material.

**Independent Test**: Can be fully tested by verifying that every answer includes accurate chunk IDs that map to actual book content.

**Acceptance Scenarios**:

1. **Given** a chatbot response with citations, **When** an instructor checks the cited chunk IDs, **Then** each citation points to the actual source passage that supports the answer.
2. **Given** a user wants to read more about a topic, **When** they click a citation, **Then** they are navigated to the relevant book section.

---

### Edge Cases

- What happens when a book version is updated?
  - New ingestion creates new version with new chunk IDs; old versions remain accessible for audit.
- How does the system handle very short queries (single words)?
  - Query normalization applies; system handles gracefully with appropriate response.
- What happens during Qdrant or Neon outages?
  - Health endpoint reports status; graceful degradation with user-friendly error messages.
- How does the system handle concurrent requests during high traffic?
  - Neon pooling + rate limiting prevents connection exhaustion.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST support two modes: BOOK mode (retrieval-based) and SELECTED_TEXT mode (highlight-based).
- **FR-002**: In BOOK mode, the system MUST retrieve relevant chunks from Qdrant based on semantic similarity.
- **FR-003**: In SELECTED_TEXT mode, the system MUST bypass retrieval and use only the provided selected text as context.
- **FR-004**: All answers MUST include citations to chunk IDs used in generating the response.
- **FR-005**: If the answer cannot be supported by the context, the system MUST respond with "Not found in the textbook" (BOOK mode) or "Not found in selected text" (SELECTED_TEXT mode).
- **FR-006**: The system MUST use Google Gemini for answer generation via generateContent or streamGenerateContent.
- **FR-007**: The system MUST use Qdrant Cloud for vector storage of book chunk embeddings.
- **FR-008**: The system MUST use Neon Postgres for metadata storage (book versions, chunks, sessions, query logs).
- **FR-009**: Content ingestion MUST produce deterministic chunk IDs: v{book_version}:ch{chapter_idx}:sec{section_idx}:p{para_idx}.
- **FR-010**: Chunk size MUST be ~300–800 tokens with 10–15% overlap between chunks.
- **FR-011**: The system MUST use Docusaurus as the book platform with embedded chat widget.
- **FR-012**: The system MUST capture page_url, chapter_id, section_anchor for both modes.
- **FR-013**: Selected text mode MUST capture selected_text, page_url, anchor, and selection_hash.
- **FR-014**: The system MUST support streaming responses via streamGenerateContent for better UX.
- **FR-015**: The system MUST implement rate limiting per IP/session.
- **FR-016**: The system MUST never expose Gemini API key to clients.
- **FR-017**: The system MUST log all queries and retrievals in Neon for auditability.

### Key Entities

- **BookVersion**: Represents a version of the book (git SHA or semantic version). Attributes: id, git_sha, created_at. Related to Chunks and IngestRuns.
- **Chunk**: A segment of book content with embedding. Attributes: chunk_id, book_version_id, chapter, section_anchor, source_path, text_hash, embedding_vector. Related to BookVersion.
- **IngestRun**: A content ingestion execution. Attributes: id, book_version_id, status, metrics_json, started_at, finished_at.
- **Session**: A user chat session. Attributes: id, created_at, last_seen_at, user_agent. Related to QueryLogs.
- **QueryLog**: A record of a user query. Attributes: id, session_id, mode, question, retrieved_chunk_ids, latency_ms, created_at.
- **SelectionRecord**: A record of selected text usage. Attributes: id, session_id, selected_text_hash, page_url, selection_offsets, created_at.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of BOOK mode answers include at least one citation to a retrieved chunk.
- **SC-002**: 100% of SELECTED_TEXT mode answers are derived only from the provided selection (verified via automated checks).
- **SC-003**: Refusal accuracy: 100% of out-of-scope questions receive "Not found" response without hallucination.
- **SC-004**: Retrieval latency p50 < 500ms, p95 < 1s (excluding Gemini generation).
- **SC-005**: Gemini generation latency p50 < 2s, p95 < 5s for streaming responses.
- **SC-006**: System handles 100 concurrent requests without degradation (verified via load testing).
- **SC-007**: Citation completeness: 100% of answers that should have citations include them.
- **SC-008**: Chunk reproducibility: Same book version produces identical chunk IDs across ingestion runs.
- **SC-009**: Evaluation set: 30-50 Q/A pairs achieve >90% accuracy on grounded answers.
- **SC-010**: Selected Text mode: 10+ tests achieve 100% accuracy on selection-only answers.

## Assumptions

- Book content is available as Markdown/MDX files (Docusaurus format).
- Gemini API access is available via Google AI for Developers.
- Qdrant Cloud free tier is sufficient for the book's vector storage needs (~1M vectors of 768 dims).
- Neon connection pooling (PgBouncer) is configured for serverless concurrency.
- Docusaurus site allows custom React components for the chat widget.
- Book content changes are versioned via git.

## Scope Boundaries

### In Scope

- Docusaurus book site integration (site-wide widget + per-page context)
- FastAPI backend service for RAG operations
- Qdrant vector database for chunk embeddings
- Neon Postgres for metadata and audit logs
- Google Gemini for answer generation
- Two-mode operation (BOOK and SELECTED_TEXT)
- Deterministic chunking with versioned ingestion
- Citation system with chunk ID references
- Session management and query logging
- Rate limiting and basic security

### Out of Scope

- Multi-book support (single book only initially)
- User authentication system
- Payment or subscription integration
- Voice-based queries
- Image-based queries
- Multi-language support
- Real-time collaboration features
- Analytics dashboard beyond basic metrics
