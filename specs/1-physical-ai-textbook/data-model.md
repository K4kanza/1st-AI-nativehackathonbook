# Data Model: Physical AI & Humanoid Robotics Textbook

## Core Entities

### Chapter
- **Attributes**:
  - id: unique identifier for the chapter
  - title: the chapter title
  - number: sequential chapter number (1-10 as per constitution)
  - word_count: number of words (1,000-1,500 as per constitution)
  - overview: brief summary of the chapter content
  - key_definitions: list of important terms defined in the chapter
  - equations: list of mathematical equations with explanations
  - real_world_examples: practical examples illustrating concepts
  - chapter_summary: comprehensive summary of the chapter
  - review_questions: list of questions for student assessment
  - exercises: list of exercises or mini-projects
  - sources: list of sources cited in the chapter
- **Relationships**:
  - Contains multiple Sections
  - References multiple Citations
  - Belongs to one Textbook

### Section
- **Attributes**:
  - id: unique identifier for the section
  - title: the section title
  - content: the main content of the section
  - anchor: internal reference anchor for linking
  - chapter_id: reference to the parent chapter
- **Relationships**:
  - Belongs to one Chapter
  - Contains multiple ContentBlocks

### ContentBlock
- **Attributes**:
  - id: unique identifier for the content block
  - type: type of content (text, equation, figure, example, definition)
  - content: the actual content
  - position: ordering within the parent section
  - section_id: reference to the parent section
- **Relationships**:
  - Belongs to one Section

### Citation
- **Attributes**:
  - id: unique identifier for the citation
  - type: source type (peer_reviewed, academic_book, official_doc, technical_report)
  - apa_reference: full APA format reference
  - in_text_citation: in-text citation format
  - source_url: URL to the source (if available)
  - verified: boolean indicating if the citation has been verified
  - chapter_id: reference to the chapter where it's used
- **Relationships**:
  - Belongs to one or more Chapters
  - Referenced by multiple ContentBlocks

### Textbook
- **Attributes**:
  - id: unique identifier for the textbook
  - title: "Physical AI & Humanoid Robotics"
  - word_count: total word count (aggregated from chapters)
  - total_sources: total number of sources cited
  - peer_reviewed_sources: count of peer-reviewed sources
  - grade_level: Flesch-Kincaid grade level
  - plagiarism_status: boolean indicating if plagiarism check passed
  - academic_review_status: status of academic peer review
- **Relationships**:
  - Contains multiple Chapters
  - References multiple Citations

## Validation Rules

### Chapter Validation
- Word count must be between 1,000 and 1,500 words
- Must include all required pedagogical elements as specified in the constitution
- Must contain at least one citation from a peer-reviewed source
- Must include all required sections: overview, key definitions, equations with intuition, real-world examples, summary, review questions, and exercises

### Citation Validation
- At least 50% of citations must be from peer-reviewed sources
- All citations must follow APA format
- Each citation must be linked to at least one ContentBlock
- Citation must be verified as accurate and accessible

### ContentBlock Validation
- Content must be academically rigorous and appropriate for computer science audience
- Mathematical equations must be properly formatted with LaTeX
- Examples must be relevant to Physical AI or humanoid robotics
- Content must be traceable to authoritative sources

### Textbook Validation
- Total word count must be appropriate for 10 chapters of 1,000-1,500 words each
- Must contain at least 15 sources across all chapters
- At least 50% of total sources must be peer-reviewed
- Must achieve Flesch-Kincaid grade level of 10-12
- Must pass plagiarism detection with 0% unattributed content
- Must include all required sections as specified in the constitution

## State Transitions

### Chapter States
- Draft → In Review → Approved → Published
- If plagiarism detected: Published → Revision Required
- If citation issues: Approved → Revision Required

### Textbook States
- In Development → In Review → Approved → Ready for Publication
- If plagiarism detected: Ready for Publication → Revision Required
- If academic review fails: Approved → Revision Required