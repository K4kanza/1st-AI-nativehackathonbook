# Tasks: Physical AI & Humanoid Robotics Book

**Input**: Design documents from `/specs/001-ai-robotics-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md (pending)
**Tests**: Build validation and content review tasks included

**Organization**: Tasks grouped by user story for independent completion and testing

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Docusaurus Project Initialization)

**Goal**: Establish the foundational Docusaurus project and core content hierarchy

- [ ] T001 Initialize Docusaurus project using `npx create-docusaurus@latest book classic`
- [ ] T002 Configure Docusaurus theme as "classic" in `book/docusaurus.config.js`
- [ ] T003 Set up sidebar auto-generation in `book/sidebars.js`
- [ ] T004 Configure GitHub Pages deployment in `book/docusaurus.config.js`
- [ ] T005 Configure math support (KaTeX) in `book/docusaurus.config.js`
- [ ] T006 Create custom CSS theme in `book/src/css/custom.css`

---

## Phase 2: Foundation & Skeleton (Directory Structure)

**Goal**: Create full Docusaurus architecture with all folders and category files

### Module 1: Foundations Skeleton

- [ ] T007 Create `_category_.json` for `book/docs/module-1-foundations/`
- [ ] T008 Create `book/docs/module-1-foundations/chapter-1-physical-ai/_category_.json`
- [ ] T009 Create `book/docs/module-1-foundations/chapter-2-math-foundations/_category_.json`
- [ ] T010 Create `book/docs/module-1-foundations/chapter-3-robot-overview/_category_.json`
- [ ] T011 Create empty lesson files in `book/docs/module-1-foundations/chapter-1-physical-ai/`
- [ ] T012 Create empty lesson files in `book/docs/module-1-foundations/chapter-2-math-foundations/`
- [ ] T013 Create empty lesson files in `book/docs/module-1-foundations/chapter-3-robot-overview/`

### Module 2: Kinematics & Dynamics Skeleton

- [ ] T014 Create `_category_.json` for `book/docs/module-2-kinematics-dynamics/`
- [ ] T015 Create `book/docs/module-2-kinematics-dynamics/chapter-1-forward-inverse-kinematics/_category_.json`
- [ ] T016 Create `book/docs/module-2-kinematics-dynamics/chapter-2-dynamics/_category_.json`
- [ ] T017 Create `book/docs/module-2-kinematics-dynamics/chapter-3-jacobians/_category_.json`
- [ ] T018 [P] Create empty lesson files in `book/docs/module-2-kinematics-dynamics/`

### Module 3: Control Systems Skeleton

- [ ] T019 Create `_category_.json` for `book/docs/module-3-control-systems/`
- [ ] T020 [P] Create chapter category files for `book/docs/module-3-control-systems/`
- [ ] T021 [P] Create empty lesson files in `book/docs/module-3-control-systems/`

### Module 4: Perception & AI Skeleton

- [ ] T022 Create `_category_.json` for `book/docs/module-4-perception-ai/`
- [ ] T023 [P] Create chapter category files for `book/docs/module-4-perception-ai/`
- [ ] T024 [P] Create empty lesson files in `book/docs/module-4-perception-ai/`

### Module 5: Motion & Planning Skeleton

- [ ] T025 Create `_category_.json` for `book/docs/module-5-motion-planning/`
- [ ] T026 [P] Create chapter category files for `book/docs/module-5-motion-planning/`
- [ ] T027 [P] Create empty lesson files in `book/docs/module-5-motion-planning/`

### Module 6: ROS2 & Software Skeleton

- [ ] T028 Create `_category_.json` for `book/docs/module-6-ros2-software/`
- [ ] T029 [P] Create chapter category files for `book/docs/module-6-ros2-software/`
- [ ] T030 [P] Create empty lesson files in `book/docs/module-6-ros2-software/`

### Module 7: Simulation Skeleton

- [ ] T031 Create `_category_.json` for `book/docs/module-7-simulation/`
- [ ] T032 [P] Create chapter category files for `book/docs/module-7-simulation/`
- [ ] T033 [P] Create empty lesson files in `book/docs/module-7-simulation/`

### Module 8: Advanced & Ethics Skeleton

- [ ] T034 Create `_category_.json` for `book/docs/module-8-advanced-ethics/`
- [ ] T035 [P] Create chapter category files for `book/docs/module-8-advanced-ethics/`
- [ ] T036 [P] Create empty lesson files in `book/docs/module-8-advanced-ethics/`

### React Components Skeleton

- [ ] T037 Create `book/src/components/RobotDiagram.jsx`
- [ ] T038 Create `book/src/components/IsaacSimViewer.jsx`
- [ ] T039 Create `book/src/components/PhysicsAnimation.jsx`

### Static Assets Structure

- [ ] T040 Create `book/static/img/diagrams/` directory
- [ ] T041 Create `book/static/img/robots/` directory
- [ ] T042 Create `book/static/img/charts/` directory

---

## Phase 3: User Story 1 - Student Self-Study (Priority: P1) MVP

**Goal**: Module 1 content - Foundations of Physical AI and humanoid robotics

**Independent Test**: Student completes end-of-chapter assessments with 80%+ accuracy

### Chapter 1: Physical AI

- [ ] T043 [US1] Write `book/docs/module-1-foundations/chapter-1-physical-ai/lesson-1-definition.md`
- [ ] T044 [US1] Write `book/docs/module-1-foundations/chapter-1-physical-ai/lesson-2-embodied-intelligence.md`
- [ ] T045 [US1] Write `book/docs/module-1-foundations/chapter-1-physical-ai/lesson-3-history-evolution.md`

### Chapter 2: Math Foundations

- [ ] T046 [US1] Write `book/docs/module-1-foundations/chapter-2-math-foundations/lesson-1-linear-algebra.md`
- [ ] T047 [US1] Write `book/docs/module-1-foundations/chapter-2-math-foundations/lesson-2-calculus-robotics.md`
- [ ] T048 [US1] Write `book/docs/module-1-foundations/chapter-2-math-foundations/lesson-3-probability-stats.md`

### Chapter 3: Robot Overview

- [ ] T049 [US1] Write `book/docs/module-1-foundations/chapter-3-robot-overview/lesson-1-humanoid-types.md`
- [ ] T050 [US1] Write `book/docs/module-1-foundations/chapter-3-robot-overview/lesson-2-anatomy.md`
- [ ] T051 [US1] Write `book/docs/module-1-foundations/chapter-3-robot-overview/lesson-3-applications.md`

### Visuals for Module 1

- [ ] T052 [US1] Add diagrams to `book/static/img/diagrams/` for Module 1
- [ ] T053 [US1] Add robot images to `book/static/img/robots/` for Module 1

### Build Validation

- [ ] T054 [US1] Run `npm run build` to validate Module 1 content
- [ ] T055 [US1] Verify sidebar hierarchy renders correctly for Module 1

**Checkpoint**: MVP complete - students can self-study Module 1 content

---

## Phase 4: User Story 2 - Instructor Course Adoption (Priority: P2)

**Goal**: Modules 2-4 content - Kinematics, Control Systems, Perception & AI

**Independent Test**: Instructor confirms 8-module structure maps to 15-week semester

### Module 2: Kinematics & Dynamics

- [ ] T056 [US2] Write all 9 lessons in `book/docs/module-2-kinematics-dynamics/`
- [ ] T057 [US2] Add math equations and diagrams for kinematics content

### Module 3: Control Systems

- [ ] T058 [US2] Write all 9 lessons in `book/docs/module-3-control-systems/`
- [ ] T059 [US2] Add control theory diagrams and examples

### Module 4: Perception & AI

- [ ] T060 [US2] Write all 9 lessons in `book/docs/module-4-perception-ai/`
- [ ] T061 [US2] Add perception diagrams and algorithm pseudocode

### Visuals for Modules 2-4

- [ ] T062 [US2] Add diagrams to `book/static/img/diagrams/` for Modules 2-4
- [ ] T063 [US2] Add charts to `book/static/img/charts/` for quantitative content

### Build Validation

- [ ] T064 [US2] Run `npm run build` to validate Modules 2-4 content
- [ ] T065 [US2] Verify all sidebar hierarchies render correctly

**Checkpoint**: Instructor can adopt full semester course (Modules 1-4)

---

## Phase 5: User Story 3 - Researcher Reference Use (Priority: P3)

**Goal**: Modules 5-8 content - Motion Planning, ROS2, Simulation, Ethics

**Independent Test**: Researcher confirms mathematical derivations and citations are accurate

### Module 5: Motion & Planning

- [ ] T066 [US3] Write all 9 lessons in `book/docs/module-5-motion-planning/`
- [ ] T067 [US3] Include complete mathematical derivations with intermediate steps

### Module 6: ROS2 & Software

- [ ] T068 [US3] Write all 9 lessons in `book/docs/module-6-ros2-software/`
- [ ] T069 [US3] Add ROS2 architecture diagrams and code examples

### Module 7: Simulation

- [ ] T070 [US3] Write all 9 lessons in `book/docs/module-7-simulation/`
- [ ] T071 [US3] Add NVIDIA Isaac Sim integration examples

### Module 8: Advanced & Ethics

- [ ] T072 [US3] Write all 9 lessons in `book/docs/module-8-advanced-ethics/`
- [ ] T073 [US3] Add VLA model coverage and ethics discussion

### Visuals for Modules 5-8

- [ ] T074 [US3] Add diagrams to `book/static/img/diagrams/` for Modules 5-8
- [ ] T075 [US3] Add simulation screenshots to `book/static/img/robots/`

### Build Validation

- [ ] T076 [US3] Run `npm run build` to validate all content
- [ ] T077 [US3] Verify complete sidebar hierarchy

**Checkpoint**: Complete textbook ready for researcher reference

---

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Final validation, citation audit, and performance optimization

### Citation Verification

- [ ] T078 Audit all citations for minimum 50% peer-reviewed sources
- [ ] T079 Verify APA 7th edition format for all references
- [ ] T080 Cross-check all factual claims against cited sources

### Build & Performance

- [ ] T081 Run full `npm run build` and fix any warnings
- [ ] T082 Verify local build time under 5 minutes
- [ ] T083 Optimize any slow-loading images or components

### Content Review

- [ ] T084 Review all technical terminology for consistent definition on first use
- [ ] T085 Verify Flesch-Kincaid grade level 10-12 for all content
- [ ] T086 Ensure all equations include intermediate steps or citations

### GitHub Pages Deployment

- [ ] T087 Configure CI/CD for GitHub Pages deployment
- [ ] T088 Test deployment pipeline

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundation (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-5)**: All depend on Foundation completion
  - User stories can proceed in parallel (if team capacity allows)
  - Or sequentially in priority order (US1 → US2 → US3)
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundation - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundation - May integrate with US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundation - May integrate with US1/US2 but independently testable

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundation tasks marked [P] can run in parallel
- Once Foundation phase completes, all user stories can start in parallel
- Different modules within a user story can be written in parallel
- Visuals (T052, T062, T074) can be created in parallel with content writing

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundation
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test against acceptance criteria
5. Deploy/demo if ready (basic textbook with Module 1)

### Incremental Delivery

1. Complete Setup + Foundation → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Complete Phase 6: Polish → Final textbook

### Parallel Team Strategy

With multiple content writers:

1. Team completes Phase 1: Setup and Phase 2: Foundation together
2. Once Foundation is done:
   - Writer A: Focuses on User Story 1 (Module 1)
   - Writer B: Focuses on User Story 2 (Modules 2-4)
   - Writer C: Focuses on User Story 3 (Modules 5-8)
3. Phase 6: Polish done by dedicated reviewer or distributed

---

## Task Summary

| Phase | Description | Task Count |
|-------|-------------|------------|
| Phase 1 | Setup | 6 tasks |
| Phase 2 | Foundation & Skeleton | 42 tasks |
| Phase 3 | User Story 1 (Module 1) | 12 tasks |
| Phase 4 | User Story 2 (Modules 2-4) | 10 tasks |
| Phase 5 | User Story 3 (Modules 5-8) | 10 tasks |
| Phase 6 | Polish & Cross-Cutting | 11 tasks |
| **Total** | | **91 tasks** |

---

## Notes

- [P] tasks = different files, no dependencies - can be run in parallel
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each lesson or logical group
- Stop at any checkpoint to validate story independently
- Citations must be verified throughout content creation
