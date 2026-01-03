# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

## Getting Started

This guide will help you set up the environment and begin contributing to the Physical AI & Humanoid Robotics textbook project.

### Prerequisites

Before you begin, ensure you have the following installed:

- Git (for version control)
- Pandoc (for PDF generation)
- LaTeX distribution (for equation rendering)
- Python 3.8+ (for quality assurance tools)
- Zotero (for citation management)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd book-ai
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   If requirements.txt doesn't exist, create it with:
   ```
   textstat>=0.7.0
   pyenchant>=3.2.0
   ```

3. **Set up LaTeX for equation rendering**
   - Install a LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
   - Verify installation: `pdflatex --version`

4. **Configure citation management**
   - Install Zotero desktop application
   - Install Zotero connector for your browser
   - Set up the project library in Zotero

### Project Structure

The textbook content is organized as follows:

```
src/
├── textbook/
│   ├── front-matter/
│   ├── chapter-1-foundations/
│   ├── chapter-2-humanoid-fundamentals/
│   ├── chapter-3-mathematics/
│   ├── chapter-4-perception/
│   ├── chapter-5-motion-control/
│   ├── chapter-6-system-integration/
│   ├── chapter-7-case-studies/
│   ├── chapter-8-ethics/
│   └── references/
├── tools/
└── build/
```

### Writing Your First Chapter

1. **Choose a chapter directory** from the `src/textbook/` folder
2. **Update the content files** following the required structure:
   - overview.md
   - content.md
   - equations.md
   - examples.md
   - summary.md
   - review-questions.md
   - exercises.md
3. **Add citations** using Zotero and ensure they follow APA format
4. **Validate your content** using the provided tools (see Quality Assurance section)

### Quality Assurance Tools

Run the following commands to ensure your content meets the project standards:

1. **Check word count and readability**:
   ```bash
   python tools/readability-analyzer.py src/textbook/chapter-X/
   ```
   Ensure Flesch-Kincaid grade level is between 10-12.

2. **Verify citations**:
   ```bash
   python tools/citation-checker.py src/textbook/chapter-X/
   ```
   Ensure at least 50% of sources are peer-reviewed.

3. **Run plagiarism check**:
   ```bash
   python tools/plagiarism-detector.py src/textbook/chapter-X/
   ```
   Ensure 0% unattributed content.

### Building the Textbook

To generate the PDF version of the textbook:

```bash
bash build/pdf-builder.sh
```

To generate a web version:

```bash
bash build/web-exporter.sh
```

### Contributing Guidelines

1. **Follow the academic standards** outlined in the constitution
2. **Ensure all claims are cited** with authoritative sources
3. **Maintain the 10-12 grade reading level** requirement
4. **Include all required pedagogical elements** in each chapter
5. **Use LaTeX syntax** for mathematical equations
6. **Submit content for peer review** before finalizing

### Common Tasks

- **Adding a new citation**: Use Zotero to export in BibTeX format, then convert to markdown with pandoc
- **Including equations**: Use LaTeX syntax between `$...$` for inline equations or `$$...$$` for display equations
- **Adding figures**: Place images in the appropriate chapter directory and reference them in markdown
- **Creating cross-references**: Use markdown anchors and links for internal references

### Troubleshooting

- If equations don't render in PDF: Verify LaTeX installation and check equation syntax
- If citations don't appear: Verify CSL file is properly configured and Zotero export is correct
- If readability score is too high: Simplify complex sentences and replace technical jargon with explanations
- If plagiarism check fails: Verify all content is properly attributed to original sources