---
id: 0006
title: Finalize Physical AI Robotics Book Research
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

Project: Physical AI & Humanoid Robotics – Docusaurus-Based Book  
Goal: Create a production-ready Docusaurus book covering Physical AI, Embodied Intelligence, and Humanoid Robotics, structured into chapters and lessons, deployed on GitHub Pages, written using Spec-Kit-Plus.

---

## 1. Architecture Sketch

### **Core Structure**
- **Docusaurus root**
  - `/docs/` → All chapters (each with 3 lessons inside)
  - `/blog/` → Extra insights, updates, announcements
  - `/src/components/` → Custom React components for diagrams, robotics visualizations
  - `/static/images/` → Figures, robot schematics, chapter illustrations
  - `docusaurus.config.js` → Theme, navbar, footer, plugins
  - `sidebars.js` → Auto-generated sidebar for chapters/lessons

### **Book Layout**
- **Introduction**
- **Chapter 1: Physical AI Fundamentals**
  - Lesson 1.1: What is Physical AI?
  - Lesson 1.2: Embodied Intelligence Principles
  - Lesson 1.3: Physical Constraints & Real-World Dynamics
- **Chapter 2: Humanoid Robotics Basics**
  - Lesson 2.1: Humanoid Morphology
  - Lesson 2.2: Sensors & Perception
  - Lesson 2.3: Actuators & Motion Control
- **Chapter 3: Control Systems**
  - Lesson 3.1: Low-Level Control (PID, Torque Control)
  - Lesson 3.2: High-Level Control (Planning, Policies)
  - Lesson 3.3: Whole-Body Control Concepts
- **Chapter 4: AI for Robotics**
  - Lesson 4.1: Using ML in Physical Systems
  - Lesson 4.2: Reinforcement Learning for Robots
  - Lesson 4.3: Safety & Reward Design
- **Chapter 5: Simulation → Real World**
  - Lesson 5.1: Sim2Real Gap
  - Lesson 5.2: Domain Randomization Methods
  - Lesson 5.3: Real-World Deployment
- **Chapter 6: Final Capstone**
  - Lesson 6.1: Build a Physical AI Agent
  - Lesson 6.2: Control a Humanoid in Simulation
  - Lesson 6.3: Physical AI Evaluation Pipeline

---

## 2. Section Structure

Each lesson will follow:

1. **Learning Objectives**
2. **Concept Explanation**
3. **Real-World Examples**
4. **Mathematical or technical breakdown**
5. **Mini-Project**
6. **Summary**
7. **APA-style references**

---

## 3. Research Approach (Concurrent)

- Research while writing instead of doing all research up-front.
- Use:
  - Google Scholar (for Physical AI & robotics papers)
  - Boston Dynamics papers & docs
  - Stanford & MIT robotics courses
  - APA citation rules
- While drafting each chapter, research immediately when:
  - A scientific claim is made
  - A figure is added
  - Definitions require authoritative sources

---

## 4. Quality Validation

### **Validation checks**
- Follows Docusaurus formatting  
- All chapters follow 3-lesson structure  
- Every lesson contains APA references  
- Code blocks are tested  
- Equations reviewed for correctness  
- Visuals added where needed  
- Reading flow is coherent  
- No incomplete placeholders  

### **Review process**
- Initial draft → Structural review → Technical accuracy → Final polish

---

## 5. Decisions Needing Documentation

### **1. Docusaurus Theme**
Options:
- Minimal classic theme
- Custom robotics UI
- Shadcn + Tailwind integration hack

**Choice:** Classic theme (stable, minimal, no conflicts)

Tradeoff: Less customized UI but more reliable.

---

### **2. Sidebar Strategy**
Options:
- Manual sidebar
- Auto-generated from directory
- Mixed

**Choice:** Auto-generated  
Tradeoff: Requires strict folder naming.

---

### **3. Deployment**
Options:
- GitHub Pages
- Netlify
- Vercel

**Choice:** GitHub Pages (native for Docusaurus)

---

### **4. Content Format**
Options:  
- Markdown only  
- MDX with components  

**Choice:** MDX + React components  
Tradeoff: More powerful but some complexity.

---

## 6. Testing Strategy

### **Acceptance Criteria**
- Book runs on `npm start` with no warnings  
- Sidebar shows all chapters (1 to 6) + lessons (3 each)  
- Website builds successfully on GitHub Pages  
- All internal links resolve  
- The navigation flow is intuitive  
- APA citations appear correctly  

### **Testing Actions**
- Run: `npx docusaurus start` after every major change  
- Validate sidebar auto-generation  
- Check for broken links  
- Test GitHub Pages deploy with `npx docusaurus deploy`  
- Test mobile responsiveness  
- Validate search index  

---

## 7. Phase Organization

### **Phase 1 – Research**
- Gather key papers & robotics references  
- Note important diagrams & models  

### **Phase 2 – Foundation**
- Build Docusaurus project  
- Implement folder + chapter structure  
- Add introduction + Chapter 1  

### **Phase 3 – Analysis**
- Deep technical writing  
- Add code, diagrams, lessons 2–5  

### **Phase 4 – Synthesis**
- Capstone chapter  
- Final review  
- Deploy to GitHub Pages

## Response snapshot

The `research.md` file (`specs/1-ai-robotics-book/research.md`) has been fully resolved with decisions regarding hardware selection, simulation platform, and NLP/LLM integration. The implementation plan (`specs/1-ai-robotics-book/plan.md`) remains as previously updated.

## Outcome

- ✅ Impact: Phase 0 research is complete and all decisions have been documented. The plan is ready for Phase 1 design.
- 🧪 Tests: None (documentation update)
- 📁 Files: Updated specs/1-ai-robotics-book/research.md
- 🔁 Next prompts: The plan is ready for Phase 1 design, which involves generating `data-model.md`, `contracts/`, and `quickstart.md`.
- 🧠 Reflection: Successfully finalized all research questions, bringing the planning phase to a robust state.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
