---
description: "Task list for RAG Chatbot implementation"
---

# Tasks: RAG Chatbot for Book

**Input**: Design documents from `/specs/002-rag-chatbot-book/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/
**Tests**: Unit and integration tests required for all user stories

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/`, `backend/tests/`
- **Frontend**: `frontend/src/`, `frontend/tests/`
- **Database**: `backend/src/db/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend project structure per plan.md (backend/src/, backend/tests/, scripts/)
- [ ] T002 Initialize Python 3.11+ project with FastAPI, Google GenerativeAI SDK, qdrant-client, asyncpg
- [ ] T003 [P] Configure pyproject.toml with dependencies, version, and Python 3.11+ requirement
- [ ] T004 [P] Configure ruff for linting and formatting
- [ ] T005 [P] Configure pytest with pytest-asyncio, httpx for API tests
- [ ] T006 Create environment configuration (.env.example) with all required env vars
- [ ] T007 Create Dockerfile for backend service
- [ ] T008 Create docker-compose.yml for local development (Qdrant, optional local Postgres)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T009 Setup Neon database schema from data-model.md (create tables, indexes, enums)
- [ ] T010 Create database connection module in backend/src/db/connection.py (asyncpg with pooling)
- [ ] T011 [P] Implement SQLAlchemy or raw SQL models for all entities from data-model.md
- [ ] T012 [P] Create Pydantic schemas in backend/src/db/schemas.py for request/response validation
- [ ] T013 Setup FastAPI application structure in backend/src/api/routes.py
- [ ] T014 Configure CORS middleware for Docusaurus domain
- [ ] T015 Create health check endpoint in backend/src/api/routes.py (checks Gemini, Qdrant, Neon)
- [ ] T016 Implement environment configuration loading in backend/src/config.py
- [ ] T017 [P] Setup logging infrastructure with structured JSON logs
- [ ] T018 Implement rate limiting middleware (60 requests per minute per IP)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Book Mode Query (Priority: P1) 🎯 MVP

**Goal**: Users can ask questions about book content and receive answers grounded in retrieved chunks with citations

**Independent Test**: Users ask questions about book content and receive answers with citations to specific chunks

### Tests for User Story 1 ⚠️

> NOTE: Write these tests FIRST, ensure they FAIL before implementation

- [ ] T019 [P] [US1] Contract test for POST /rag/query in backend/tests/contract/test_query.py
- [ ] T020 [P] [US1] Integration test for BOOK mode retrieval flow in backend/tests/integration/test_book_mode.py
- [ ] T021 [P] [US1] Unit test for chunker service in backend/tests/unit/test_chunker.py

### Implementation for User Story 1

- [ ] T022 [P] [US1] Implement chunker service in backend/src/ingest/chunker.py (semantic chunking 300-800 tokens)
- [ ] T023 [P] [US1] Implement embedding service in backend/src/services/embedding.py (sentence-transformers or Gemini embeddings)
- [ ] T024 [US1] Implement Qdrant service in backend/src/services/qdrant.py (vector search, upsert, filtering)
- [ ] T025 [US1] Implement Gemini service in backend/src/services/gemini.py (generateContent with citations)
- [ ] T026 [US1] Create RAG orchestrator in backend/src/services/rag.py (BOOK mode logic)
- [ ] T027 [US1] Implement POST /rag/query endpoint in backend/src/api/routes.py (BOOK mode handler)
- [ ] T028 [US1] Add citation extraction and formatting in Gemini service
- [ ] T029 [US1] Add "Not found in the textbook" response for out-of-scope queries
- [ ] T030 [US1] Add chunk retrieval logging to query_logs table

**Checkpoint**: BOOK mode should be functional and testable independently

---

## Phase 4: User Story 2 - Selected Text Only Mode (Priority: P2)

**Goal**: Users can highlight text and get answers strictly grounded in their selection

**Independent Test**: Highlighting a passage and asking questions returns answers only from that passage

### Tests for User Story 2 ⚠️

- [ ] T031 [P] [US2] Integration test for SELECTED_TEXT mode in backend/tests/integration/test_selected_text_mode.py
- [ ] T032 [P] [US2] Unit test for selected text guardrails in backend/tests/unit/test_guardrails.py

### Implementation for User Story 2

- [ ] T033 [US2] Add SELECTED_TEXT mode handler in RAG orchestrator (bypass retrieval)
- [ ] T034 [US2] Implement strict context-only prompt in Gemini service for selected text mode
- [ ] T035 [US2] Implement "Not found in selected text" response guardrail
- [ ] T036 [US2] Add selected_text_hash calculation and storage to selection_records table
- [ ] T037 [US2] Update POST /rag/query endpoint to handle selected_text parameter
- [ ] T038 [US2] Add validation: reject empty or too-long selected text

**Checkpoint**: Both BOOK and SELECTED_TEXT modes should work independently

---

## Phase 5: User Story 3 - Citation and Traceability (Priority: P3)

**Goal**: All answers include accurate citations that map to actual book content with clickable navigation

**Independent Test**: Citations in responses point to real chunks that support the answers

### Tests for User Story 3 ⚠️

- [ ] T039 [P] [US3] Test citation completeness (95% of answers have citations)
- [ ] T040 [P] [US3] Test citation accuracy (cited chunks actually contain supporting content)

### Implementation for User Story 3

- [ ] T041 [US3] Enhance citation format in Gemini service responses
- [ ] T042 [US3] Create citation struct with chunk_id, chapter_title, section_anchor, source_path
- [ ] T043 [US3] Add citation validation: verify cited chunks contain answer content
- [ ] T044 [US3] Implement citation click-through URL generation (maps anchor to page)
- [ ] T045 [US3] Add citation logging to query_logs.citations field

**Checkpoint**: All three user stories should work and citations should be complete and accurate

---

## Phase 6: Backend Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T046 [P] Implement streaming responses via streamGenerateContent for better UX
- [ ] T047 [P] Add session management (POST /chat/session endpoint, sessions table)
- [ ] T048 [P] Implement ingestion CLI in backend/src/ingest/cli.py (markdown to chunks to Qdrant)
- [ ] T049 [P] Add deterministic chunk ID generation (v{version}:ch{idx}:sec{idx}:p{idx})
- [ ] T050 [P] Implement book version tracking with git_sha storage
- [ ] T051 Add retry logic for transient failures (Gemini, Qdrant, Neon)
- [ ] T052 Add comprehensive error handling with user-friendly messages
- [ ] T053 Security hardening: validate all inputs, sanitize user content
- [ ] T054 [P] Add unit tests for all services (chunker, embedding, qdrant, gemini, rag)
- [ ] T055 [P] Add integration tests for all API endpoints
- [ ] T056 Run full test suite and fix any failures
- [ ] T057 Validate quickstart.md setup works end-to-end

---

## Phase 7: Frontend Integration (Docusaurus Widget)

**Purpose**: Embedded chat UI in Docusaurus book site

- [ ] T058 Create frontend project structure (frontend/src/components/, frontend/src/hooks/)
- [ ] T059 Implement ChatWidget React component in frontend/src/components/ChatWidget.jsx
- [ ] T060 [P] Implement useChat hook for API communication in frontend/src/hooks/useChat.js
- [ ] T061 [P] Implement text selection capture using Browser Selection API
- [ ] T062 Add "Selected Text Only" toggle UI in chat widget
- [ ] T063 Implement chat message display (question/answer pairs with citations)
- [ ] T064 Add citation click-through navigation to book sections
- [ ] T065 Integrate widget into Docusaurus layout (src/theme/Root.js)
- [ ] T066 Test widget on sample Docusaurus pages
- [ ] T067 Add frontend tests for widget interactions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all user stories being complete
- **Frontend (Phase 7)**: Can start after Phase 3 (BOOK mode core) completes

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Phase 2 - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Phase 2 - Depends on US1 (citation extraction requires retrieval)

### Within Each User Story

- Tests (T019-T021, T031-T032, T039-T040) MUST be written and FAIL before implementation
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Stories 1, 2, and 3 can start in parallel
- All tests for a user story marked [P] can run in parallel
- Frontend tasks marked [P] can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test BOOK mode independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Polish → Finalize
6. Add Frontend Integration → Complete

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (BOOK mode core)
   - Developer B: User Story 2 (Selected Text mode)
   - Developer C: User Story 3 (Citations)
3. Stories complete and integrate independently
4. Add frontend integration

---

## Evaluation Checklist (Run after implementation)

- [ ] SC-001: 95% of BOOK mode answers include citations (test with 30-50 Q/A pairs)
- [ ] SC-002: 100% of SELECTED_TEXT answers use only selected text
- [ ] SC-003: Out-of-scope questions receive "Not found" response
- [ ] SC-004: Retrieval latency p50 < 500ms
- [ ] SC-005: Gemini generation latency p50 < 2s streaming
- [ ] SC-006: System handles 100 concurrent requests
- [ ] SC-008: Chunk reproducibility verified
- [ ] All unit tests pass (>80% coverage)
- [ ] All integration tests pass
- [ ] API contract tests pass (OpenAPI validation)
- [ ] Frontend widget renders correctly in Docusaurus

---

## Notes

- **[P]** tasks = different files, no dependencies
- **[Story]** label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
