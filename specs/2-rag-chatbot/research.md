# Research: Integrated RAG Chatbot for Book

## Decision Log

### 1. Tech Stack Selection
**Decision**: Use the specified tech stack (Gemini, FastAPI, Neon, Qdrant)
**Rationale**: The user explicitly specified these technologies, which form a solid RAG architecture with a powerful LLM
**Alternatives considered**:
- OpenAI + Supabase + PostgreSQL (would require different API keys and contracts)
- Azure AI + CosmosDB (vendor lock-in concerns, different pricing model)
- Open-source alternatives (Llama + PGVector) (would require more infrastructure management)

### 2. Chunking Strategy
**Decision**: Chapter → Section → Paragraph chunking with overlap
**Rationale**: This follows the natural document structure while preserving context between chunks
**Alternatives considered**:
- Fixed token length chunks (might break semantic boundaries)
- Sentence-level chunks (too granular for meaningful responses)
- Custom chunking based on semantic meaning (more complex implementation)

### 3. Citation Format
**Decision**: Include chunk_id, chapter, section, and source path in citations
**Rationale**: Provides sufficient information for users to locate the original content
**Alternatives considered**:
- Page numbers only (not suitable for digital documents)
- Paragraph numbers (not stable across edits)
- Anchor links (requires more complex processing)

### 4. Frontend Integration Approach
**Decision**: React-based widget embedded in Docusaurus layout
**Rationale**: Provides rich interactivity while being compatible with the static site generator
**Alternatives considered**:
- Vanilla JavaScript widget (less maintainable, more code needed)
- Iframe embedding (more complex communication, styling limitations)
- Server-side rendering (not compatible with static site approach)

### 5. Selected Text Mode Implementation
**Decision**: Capture highlighted text via browser selection API and send to backend
**Rationale**: Provides precise control over context while being straightforward to implement
**Alternatives considered**:
- Client-side search in document (less reliable, potential performance issues)
- Pre-computed text regions (would require complex preprocessing)

### 6. Session Management
**Decision**: Server-side session storage in Neon with client-side session ID
**Rationale**: Maintains conversation context while keeping user data secure
**Alternatives considered**:
- Client-only storage (limited persistence, harder to analyze usage)
- Third-party session service (additional dependency, potential cost)

## Technical Research Findings

### RAG Pipeline Best Practices
Research shows that effective RAG implementations require:
- Proper chunking to balance context preservation with retrieval precision
- Semantic search with optional re-ranking for improved relevance
- Prompt engineering to ensure the LLM only uses provided context
- Comprehensive logging for debugging and performance optimization

### Gemini API Integration
The Google Gen AI SDK provides:
- Easy integration with FastAPI applications
- Support for both text and streaming responses
- Built-in safety filters and content moderation
- Consistent performance and availability

### Vector Database Selection
Qdrant Cloud offers:
- Easy setup and management
- Good performance for semantic search
- Cost-effective free tier suitable for initial development
- Robust filtering capabilities for metadata

### Database Connection Pooling
Neon's built-in connection pooling (PgBouncer) provides:
- Efficient resource utilization
- Stable performance under load
- Serverless scalability
- Reduced connection overhead

## Implementation Notes

The research confirms that the selected approach aligns with RAG best practices while meeting the specific requirements of the book integration. The chosen tools support both the functional requirements (book-only answers, selected text mode) and non-functional requirements (performance, scalability) specified in the feature requirements.