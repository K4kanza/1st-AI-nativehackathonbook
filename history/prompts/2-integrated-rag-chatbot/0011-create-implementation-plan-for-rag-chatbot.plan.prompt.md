---
id: 0011
title: Create Implementation Plan for RAG Chatbot
stage: plan
date: 2025-12-16
surface: agent
model: gemini-pro
feature: 2-integrated-rag-chatbot
branch: 2-integrated-rag-chatbot
user: 
command: /sp.plan
labels: [planning, architecture, rag]
links:
  spec: specs/2-integrated-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-integrated-rag-chatbot/plan.md
- specs/2-integrated-rag-chatbot/research.md
- specs/2-integrated-rag-chatbot/data-model.md
- GEMINI.md
tests:
- none
---

## Prompt

/sp.plan

Create a detailed implementation plan for the feature **"Integrated RAG Chatbot"** using the existing specification:

- specs/2-integrated-rag-chatbot/spec.md
- specs/2-integrated-rag-chatbot/checklists/requirements.md

The plan MUST strictly follow the approved specification and MUST NOT change scope.

---

## Mandatory Technology Stack (LOCKED)

### LLM & AI
- **Primary LLM**: Google **Gemini**
- **Embeddings**: **Cohere** embedding models
- **Agent / Orchestration Layer**: **OpenAI Agent SDK**
  - Agent logic, tool usage, retrieval grounding, and response generation MUST be implemented using OpenAI Agent SDK

### Backend
- **FastAPI**
- **Neon Serverless Postgres**
  - Chat sessions
  - Chat history
  - Metadata and analytics

### Vector Database
- **Qdrant Cloud (Free Tier)**
  - Stores Cohere-generated embeddings
  - Used for similarity search and retrieval

### Frontend
- Embedded chat interface inside the book pages
- Supports:
  - Full-book questions
  - Selected-text–only questions

---

## RAG Pipeline Responsibility (MANDATORY)

The system is fully responsible for:
- Book ingestion
- Text chunking
- Embedding generation (via Cohere)
- Vector storage (Qdrant)
- Retrieval logic
- Passing retrieved context to the OpenAI Agent SDK

Users MUST NOT:
- Upload embeddings
- Configure retrieval
- Manage context manually

Users interact ONLY through the chat UI.

---

## Planning Requirements

The plan MUST include:

### 1. Architecture Overview
- High-level RAG flow (textual diagram)
- Clear separation between:
  - Frontend
  - FastAPI backend
  - Retrieval layer (Qdrant + Cohere)
  - Agent layer (OpenAI Agent SDK)
  - LLM execution (Gemini)

### 2. Data Flow & RAG Logic
- Book ingestion pipeline
- Chunking strategy (size & overlap)
- Embedding generation using Cohere
- Qdrant collection schema
- Retrieval strategy (top-k, similarity, filters)
- Differences between:
  - Full-book queries
  - Selected-text–only queries

### 3. OpenAI Agent SDK Design
- Agent responsibilities
- System prompt structure
- How retrieved chunks are injected
- Rules to ensure answers are grounded
- Behavior when answer is not present in context
- How Gemini is invoked by the agent

### 4. Backend API Plan (FastAPI)
- Endpoint list with purpose
- High-level request/response contracts
- Chat session handling
- Error and fallback handling

### 5. Frontend Integration Plan
- Chat UI states
- Selected-text capture mechanism
- Context mode switching
- Loading, empty, and error states

### 6. Milestones & Task Breakdown
- **P1**: Core RAG chatbot (entire book)
- **P2**: Selected-text contextual RAG
- Clear task lists per phase

### 7. Risks & Mitigations
- Gemini latency or quota issues
- Cohere embedding limits
- Qdrant free-tier constraints
- Context leakage or hallucination risks

---

## Output Rules (STRICT)

- Markdown only
- Clear headings
- Implementation-ready
- No speculative features
- No scope expansion
- Minimal or no code

---

## Success Condition

The plan should be detailed enough that a developer can begin implementation immediately with no open architectural questions.

Start planning now.

## Response snapshot

I have created a detailed implementation plan for the Integrated RAG Chatbot feature. This includes the architecture, data flow, API design, frontend integration, milestones, and risks. I have also created the `research.md` and `data-model.md` files, and updated the `GEMINI.md` context file.

## Outcome

- ✅ Impact: High. This sets up the entire implementation phase for the feature.
- 🧪 Tests: none
- 📁 Files: 4 files created/updated.
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The user provided very clear and detailed requirements for the plan, which made the process straightforward. The manual replication of the shell scripts is a recurring issue that needs to be addressed.

## Evaluation notes (flywheel)

- Failure modes observed: Shell script execution failures.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
