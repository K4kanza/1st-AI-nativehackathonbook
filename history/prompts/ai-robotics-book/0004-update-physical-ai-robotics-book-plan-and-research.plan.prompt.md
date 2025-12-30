---
id: 0004
title: Update Physical AI Robotics Book Plan and Research
stage: plan
date: 2025-12-05
surface: agent
model: gemini-1.5-pro
feature: ai-robotics-book
branch: main
user: current_user
command: /sp.plan
labels: ["plan", "feature-planning"]
links:
  spec: specs/1-ai-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-ai-robotics-book/plan.md
  - specs/1-ai-robotics-book/research.md
tests: []
---

## Prompt

/sp.plan /sp.plan

Create:
- Full Docusaurus book architecture (all modules, chapters, and lessons)
- Section structure for 8 modules, each with 3 chapters, each chapter with 3 lessons
- Research approach for Physical AI, ROS2, Digital Twins, VLA, Isaac Sim, and Humanoid Robotics
- Quality validation strategy aligned with the Constitution standards

Decisions needing documentation:
- Why Docusaurus was selected instead of MkDocs or GitBook
- Why book is structured into modules → chapters → lessons
- Why concurrent research is used instead of upfront research
- Why APA style and peer-reviewed sources are required
- Tradeoffs between including simulations vs. real hardware content
- Choice of keeping diagrams inside `/static` vs. per-module folders

Testing strategy:
- Validate all content builds correctly in Docusaurus (npm start → no warnings)
- Validate all images resolve and follow assets path rules
- Validate every lesson renders with correct sidebar hierarchy
- Validate citations follow APA style
- Validate chapter structure matches spec (8 modules, 24 chapters, 72 lessons)

Technical details:
- Follow Docusaurus v3 folder structure
- Use research-concurrent approach (research while writing each chapter)
- Use MDX/Markdown for chapters and lessons
- Assets stored in `/static/img/...`
- Follow Constitution rules for accuracy, clarity, reproducibility, rigor
- Every chapter requires minimum 6 verified academic sources
- Organize by phases: Phase 0 (Research), Phase 1 (Foundation & Skeleton), Phase 2 (Lesson Writing), Phase 3 (Review & Diagram Integration)

## Response snapshot

The implementation plan (`specs/1-ai-robotics-book/plan.md`) and research document (`specs/1-ai-robotics-book/research.md`) have been updated with the latest details and new decisions requiring documentation.

## Outcome

- ✅ Impact: Implementation plan further refined, and additional research questions identified.
- 🧪 Tests: None (documentation update)
- 📁 Files: Updated specs/1-ai-robotics-book/plan.md and specs/1-ai-robotics-book/research.md
- 🔁 Next prompts: User needs to provide input on the "NEEDS CLARIFICATION" items in `research.md` to proceed with further design.
- 🧠 Reflection: Successfully integrated new planning details and captured additional research questions.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
