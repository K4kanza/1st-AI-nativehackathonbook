# Tasks: Integrated RAG Chatbot for Book

**Feature**: Integrated RAG Chatbot for Book
**Created**: 2025-12-25
**Status**: Draft
**Input**: Feature specification from `/specs/2-rag-chatbot/spec.md`

## Implementation Strategy

This implementation follows an MVP-first approach with incremental delivery. Phase 1 and 2 establish the foundational infrastructure, then each user story is implemented in priority order (P1, P2, P3). Each user story phase produces a complete, independently testable increment.

## Dependencies

- **User Story 2** depends on User Story 1 (Selected Text Only mode builds on basic Q&A functionality)
- **User Story 3** depends on User Story 1 and 2 (verification requires both modes to be functional)

## Parallel Execution Examples

- T005 [P], T006 [P], T007 [P]: Set up backend, frontend, and docusaurus directories in parallel
- T015 [P], T016 [P], T017 [P]: Create different data models in parallel
- T025 [P], T026 [P], T027 [P]: Create different service modules in parallel

---

## Phase 1: Setup

**Goal**: Initialize project structure and configure development environment

- [X] T001 Create backend directory structure per implementation plan
- [X] T002 Create frontend directory structure per implementation plan
- [X] T003 Create docusaurus directory structure per implementation plan
- [X] T004 Create docs directory structure per implementation plan
- [X] T005 [P] Initialize backend requirements.txt with FastAPI, Google Gen AI SDK, Qdrant client, Neon driver
- [X] T006 [P] Initialize frontend package.json with React and required dependencies
- [X] T007 [P] Initialize docusaurus package.json and configuration
- [X] T008 Create backend/src directory structure
- [X] T009 Create frontend/src directory structure
- [X] T010 Create docusaurus/src directory structure
- [ ] T011 Set up backend virtual environment
- [X] T012 Create .env file template for backend configuration
- [X] T013 Configure environment variables for Gemini, Qdrant, and Neon

## Phase 2: Foundational

**Goal**: Implement core infrastructure components that support all user stories

- [ ] T014 Set up database models and Alembic migrations
- [ ] T015 [P] Create BookContent model in backend/src/models/book_content.py
- [ ] T016 [P] Create Chunk model in backend/src/models/chunk.py
- [ ] T017 [P] Create Session model in backend/src/models/session.py
- [ ] T018 [P] Create QueryLog model in backend/src/models/query_log.py
- [ ] T019 [P] Create IngestionRun model in backend/src/models/ingestion_run.py
- [ ] T020 Configure database connection with Neon pooling
- [ ] T021 Set up Qdrant client connection
- [ ] T022 Create initial database migration scripts in alembic/versions/
- [ ] T023 Create Pydantic models for API requests/responses
- [ ] T024 [P] Create QueryRequest model in backend/src/models/query.py
- [ ] T025 [P] Create QueryResponse model in backend/src/models/response.py
- [ ] T026 [P] Create IngestionRequest model in backend/src/models/ingestion.py
- [ ] T027 [P] Create SessionRequest model in backend/src/models/session.py
- [ ] T028 Set up FastAPI application with CORS configuration
- [ ] T029 Create main.py with FastAPI app initialization
- [ ] T030 Configure logging and health check endpoint
- [ ] T031 Implement basic configuration loading from environment variables

## Phase 3: User Story 1 - Book Reader Inquiry (P1)

**Goal**: Enable users to ask questions about book content and receive answers based only on the book's information with proper citations

**Independent Test**: Reader can ask a question and receive an answer that is grounded in the book's content with proper citations.

- [ ] T032 [US1] Create ingestion service in backend/src/services/ingestion.py
- [ ] T033 [US1] Implement content chunking utility in backend/src/utils/chunking.py
- [ ] T034 [US1] Create retrieval service in backend/src/services/retrieval.py
- [ ] T035 [US1] Create generation service in backend/src/services/generation.py
- [ ] T036 [US1] Create citation utility in backend/src/utils/citations.py
- [ ] T037 [US1] Implement ingestion endpoint in backend/src/api/rag.py
- [ ] T038 [US1] Implement basic RAG query endpoint in backend/src/api/rag.py
- [ ] T039 [US1] Add deterministic chunk ID generation following v{version}:ch{chapter_idx}:sec{section_idx}:p{para_idx} format
- [ ] T040 [US1] Implement content validation per data model requirements
- [ ] T041 [US1] Add embedding generation and storage to Qdrant
- [ ] T042 [US1] Implement retrieval from Qdrant with filtering by book version
- [ ] T043 [US1] Connect Gemini API for answer generation
- [ ] T044 [US1] Implement citation formatting in responses
- [ ] T045 [US1] Add query logging to Neon database
- [ ] T046 [US1] Create ChatWidget component in frontend/src/components/ChatWidget.jsx
- [ ] T047 [US1] Create Message component in frontend/src/components/Message.jsx
- [ ] T048 [US1] Create Citation component in frontend/src/components/Citation.jsx
- [ ] T049 [US1] Implement API service in frontend/src/services/api.js
- [ ] T050 [US1] Create useChat hook in frontend/src/hooks/useChat.js
- [ ] T051 [US1] Add basic styling for chat widget in frontend/src/styles/chat.css
- [ ] T052 [US1] Implement basic Docusaurus integration in docusaurus/src/components/EmbeddedChat.jsx
- [ ] T053 [US1] Test User Story 1 acceptance scenario 1: Question with book-based answer and citations
- [ ] T054 [US1] Test User Story 1 acceptance scenario 2: Question with "not in book" response

## Phase 4: User Story 2 - Selected Text Focus (P2)

**Goal**: Enable users to highlight specific text and ask questions only about that text to get focused answers without interference from other book content

**Independent Test**: Reader can highlight text, ask a question, and receive an answer only from the selected text.

- [ ] T055 [US2] Enhance RAG query endpoint to support SELECTED_TEXT mode
- [ ] T056 [US2] Modify generation service to work with selected text context only
- [ ] T057 [US2] Add validation for selected text mode per data model requirements
- [ ] T058 [US2] Create SelectionHandler component in frontend/src/components/SelectionHandler.jsx
- [ ] T059 [US2] Implement text selection capture using browser selection API in frontend/src/services/selection.js
- [ ] T060 [US2] Add "Selected Text Only" toggle to ChatWidget component
- [ ] T061 [US2] Modify API service to send selected text with queries
- [ ] T062 [US2] Update Docusaurus integration to capture page context (page_url, chapter_id, section_anchor)
- [ ] T063 [US2] Test User Story 2 acceptance scenario 1: Question with selected text answer
- [ ] T064 [US2] Test User Story 2 acceptance scenario 2: Question with "not in selected text" response

## Phase 5: User Story 3 - Content Verification (P3)

**Goal**: Ensure the chatbot only provides answers based on the book content to maintain content accuracy and prevent hallucinations

**Independent Test**: The system can be verified to only respond with information from the book and provide citations for all claims.

- [ ] T065 [US3] Implement response validation to ensure all content is from book chunks
- [ ] T066 [US3] Add additional citation verification to ensure all claims are traceable
- [ ] T067 [US3] Enhance logging to track response sources and citations
- [ ] T068 [US3] Create monitoring dashboard for tracking hallucination detection
- [ ] T069 [US3] Implement content filtering to prevent external knowledge usage
- [ ] T070 [US3] Add audit logging for all queries and responses
- [ ] T071 [US3] Test User Story 3 acceptance scenario 1: External knowledge query response
- [ ] T072 [US3] Test User Story 3 acceptance scenario 2: Citation verification in responses

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Complete the implementation with cross-cutting concerns and optimizations

- [ ] T073 Implement session management with Neon database
- [ ] T074 Add rate limiting per IP/session
- [ ] T075 Implement performance monitoring and metrics
- [ ] T076 Add comprehensive error handling and user-friendly messages
- [ ] T077 Optimize response latency to meet <5s requirement
- [ ] T078 Add caching mechanisms for frequently asked questions
- [ ] T079 Implement proper cleanup for inactive sessions
- [ ] T080 Add comprehensive API documentation with OpenAPI/Swagger
- [ ] T081 Create deployment documentation in docs/deployment/deployment.md
- [ ] T082 Create runbook documentation in docs/deployment/runbook.md
- [ ] T083 Write architecture documentation in docs/deployment/architecture.md
- [ ] T084 Perform end-to-end testing across all user stories
- [ ] T085 Conduct performance testing to ensure 100+ concurrent user support
- [ ] T086 Final validation against all success criteria