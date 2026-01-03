# Implementation Plan: Integrated RAG Chatbot for Book

**Branch**: `2-rag-chatbot` | **Date**: 2025-12-25 | **Spec**: [link to spec.md](../2-rag-chatbot/spec.md)
**Input**: Feature specification from `/specs/2-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build and embed a Retrieval-Augmented Generation (RAG) chatbot inside the published book (Docusaurus site). The chatbot must answer questions only from the book's content and support a "Selected Text Only" mode that answers strictly from user-highlighted passages. The implementation will use Google Gemini, FastAPI, Neon Serverless Postgres, and Qdrant Cloud.

## Technical Context

**Language/Version**: Python 3.9+ for backend services, JavaScript/TypeScript for frontend components
**Primary Dependencies**: FastAPI, Google Gen AI SDK, Qdrant client, Neon Postgres driver, React
**Storage**: Qdrant Cloud (vector storage), Neon Serverless Postgres (metadata, sessions, logs)
**Testing**: pytest for backend, Jest for frontend, integration tests for RAG pipeline
**Target Platform**: Web application (Docusaurus site with embedded chat widget)
**Project Type**: Web application with backend API and embedded frontend widget
**Performance Goals**: <5s response time for 95% of queries, support 100+ concurrent users
**Constraints**: Must use specified tech stack (Gemini, FastAPI, Neon, Qdrant), no external knowledge sources
**Scale/Scope**: Single book integration with citation tracking, support for multiple book versions

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

This project doesn't have a specific constitution file, but the implementation must adhere to the functional requirements specified in the feature specification:
- ✅ Book-only answers: Responses must be grounded in retrieved book chunks; no external browsing
- ✅ Selected Text Only mode: Restrict answers to user-highlighted passages when requested
- ✅ Citations: Every answer includes citations to chapter/section + chunk_id
- ✅ Reproducibility: Deterministic chunk IDs, versioned ingestion, traceable retrieval logs
- ✅ Embedded UI: Chat widget integrated into the book site

## Project Structure

### Documentation (this feature)

```text
specs/2-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py          # Session management endpoints
│   │   └── rag.py           # RAG query endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chunk.py         # Chunk data model
│   │   ├── query.py         # Query data model
│   │   └── response.py      # Response data model
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ingestion.py     # Content ingestion service
│   │   ├── retrieval.py     # Content retrieval service
│   │   └── generation.py    # Gemini generation service
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── chunking.py      # Content chunking utilities
│   │   └── citations.py     # Citation generation utilities
│   └── main.py              # FastAPI application entry point
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── requirements.txt
└── alembic/
    └── versions/            # Database migration scripts

frontend/
├── src/
│   ├── components/
│   │   ├── ChatWidget.jsx      # Main chat widget component
│   │   ├── Message.jsx         # Individual message component
│   │   ├── Citation.jsx        # Citation display component
│   │   └── SelectionHandler.jsx # Text selection capture
│   ├── services/
│   │   ├── api.js             # API client
│   │   └── selection.js       # Text selection utilities
│   ├── hooks/
│   │   └── useChat.js         # Chat state management
│   └── styles/
│       └── chat.css           # Widget styling
├── tests/
│   └── components/
├── package.json
└── webpack.config.js

docusaurus/
├── src/
│   ├── components/
│   │   └── EmbeddedChat.jsx  # Docusaurus-specific chat integration
│   └── theme/
│       └── MDXComponents.js   # Extend MDX components
├── docusaurus.config.js
└── static/
    └── chat-widget/           # Built widget assets

docs/
└── deployment/
    ├── architecture.md
    ├── deployment.md
    └── runbook.md
```

**Structure Decision**: Multi-component architecture with separate backend and frontend applications, with a Docusaurus-specific integration layer. This allows for independent development and scaling of components while maintaining a clean integration with the book site.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None identified] | [N/A] | [N/A] |
