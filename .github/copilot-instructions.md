# GitHub Copilot Instructions for Academic Website

This is Giacomo Medda's academic portfolio website built with Jekyll. Follow these instructions when working on this repository.

## Project Structure

```
_projects/          # Project pages (detailed research pages)
_pages/             # Static pages (publications.md, about.md, etc.)
_layouts/           # Jekyll layouts (project-page.html, etc.)
files/              # PDF papers and downloadable files
images/projects/    # Extracted figures organized by project slug
assets/css/         # Custom stylesheets
```

## Creating Project Pages from PDFs

### Workflow

1. **Wait for user input**: Do not start until the user provides the PDF filename and project slug
2. **Extract metadata from PDF**: Title, authors, abstract, venue, DOI
3. **Extract embedded figures** from PDF using pymupdf (not page rendering/screenshots)
4. **Create the project page** following the template structure
5. **Update publications.md** to use the featured card format

### Figure Extraction Guidelines

**Primary method - Extract embedded images directly:**

```python
import pymupdf
from PIL import Image
import io

doc = pymupdf.open('files/paper.pdf')

# First, list all embedded images to identify figures
for page_num in range(doc.page_count):
    page = doc[page_num]
    images = page.get_images(full=True)
    if images:
        print(f'Page {page_num + 1}: {len(images)} images')
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            ext = base_image['ext']
            w, h = base_image['width'], base_image['height']
            size = len(base_image['image']) // 1024
            print(f'  xref={xref}, format={ext}, size={size}KB, {w}x{h}')

# Then extract specific figures by xref
xref = 301  # The xref ID of the figure
base_image = doc.extract_image(xref)
img_data = base_image['image']

# Convert to PNG if needed
img = Image.open(io.BytesIO(img_data))
img.save('images/projects/slug/figure_name.png', 'PNG')
```

**Fallback - Page rendering (only for vector graphics with no embedded images):**

```python
import pymupdf

doc = pymupdf.open('files/paper.pdf')
page = doc[page_number]

# Render at 300 DPI for high quality
scale = 300/72
mat = pymupdf.Matrix(scale, scale)

# For specific regions, use clip
clip = pymupdf.Rect(x0, y0, x1, y1)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/slug/figure_name.png')
```

**Important rules for figures:**
- **Always use `doc.extract_image(xref)` first** - this extracts the actual embedded image
- Use `page.get_images()` to list all images and their xref IDs
- Only use page rendering as a fallback for true vector graphics (charts drawn with PDF primitives)
- Skip author photos (usually small images on page 1)
- Always verify extracted figures against the PDF before using
- Include legends and subplot titles when extracting
- **NEVER delete images without explicit user confirmation**

### Project Page Template

Create files at `_projects/{slug}.md` with this structure:

```yaml
---
title: "Full Paper Title"
slug: "project-slug"
layout: project-page
date: YYYY-MM-DD
excerpt: "One-sentence description for cards/previews"
authors:
  - "Author One"
  - "Author Two"
author_links:
  "Author One": "https://author-website.com"
venue: "Conference/Journal Name (Abbreviation YEAR)"
keywords:
  - keyword1
  - keyword2
doi: "10.xxxx/xxxxx"
paperurl: "https://link-to-paper.pdf"
code: "https://github.com/repo"
abstract: |
  The full abstract from the paper.
  Can be multiple paragraphs.
bibtex: |
  @inproceedings{citation_key,
    author = {...},
    title = {...},
    ...
  }
---

<section class="project-content">
  <!-- Introduction/Motivation -->
  <h3>Section Title</h3>
  <p>Content summarizing key aspects...</p>
  
  <!-- Figures with proper captions -->
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/slug/figure.png" alt="Description" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure N:</strong> Caption from paper.
    </figcaption>
  </figure>
  
  <!-- Main Findings -->
  <h3>Main Findings</h3>
  <ul>
    <li><strong>Finding 1:</strong> Description</li>
    <li><strong>Finding 2:</strong> Description</li>
  </ul>
</section>
```

### Content Guidelines

- **Length**: Keep pages concise but informative (visitors should understand key contributions)
- **Accuracy**: All content must come directly from the PDF - **NEVER hallucinate or invent details**
- **Figures**: Select 2-4 most impactful figures that convey the main results
- **Structure**: Introduction → Method overview → Key results → Main findings
- **Writing**: Use clear, accessible language; avoid excessive jargon

## Updating publications.md

### Featured Publication Card (for projects with dedicated pages)

```html
<!-- Featured Publication: Project Name -->
<div class="featured-publication">
  <span class="pub-badge">✦ Featured Research</span>
  <div class="pub-links">
    <a href="/projects/slug/" class="pub-link primary">
      <i class="fas fa-flask"></i> Project
    </a>
    <a href="https://github.com/repo" class="pub-link secondary" target="_blank">
      <i class="fab fa-github"></i> Code
    </a>
    <a href="https://doi.org/xxx" class="pub-link secondary" target="_blank">
      <i class="ai ai-doi"></i> DOI
    </a>
  </div>
  <h3 class="pub-title">
    <a href="/projects/slug/">Paper Title</a>
  </h3>
  <div class="pub-authors">
    Author1, Author2, <strong>G. Medda</strong>, Author3
  </div>
  <div class="pub-venue">
    Venue Name <strong>(ABBREV YEAR)</strong>
  </div>
</div>
```

### Compact Entry (for publications without project pages)

```html
<div class="publication-entry">
<span class="pub-title-inline">Paper Title</span>.<br>
Author1, Author2, <strong>G. Medda</strong>.<br>
<em>Venue Name</em> <span class="pub-venue-tag">ABBREV YEAR</span>
<div class="pub-links-inline">
<a href="https://doi.org/xxx"><i class="ai ai-doi"></i> DOI</a>
</div>
</div>
```

**When to upgrade to featured**: When creating a new project page, convert the compact entry to featured format.

## Safety Rules

1. **No hallucination**: Only use information directly from the source PDF
2. **No deletions without confirmation**: Never delete files (especially images) without asking
3. **Verify figures**: Always confirm extracted images match the PDF before updating markdown
4. **Backup awareness**: The user may want to keep old/unused images for reference
5. **Test locally**: Remind user to check `localhost:4000` after changes

## File Naming Conventions

- Project slugs: lowercase with hyphens (e.g., `fa4gcf`, `cga-cfmitigation`)
- Image folders: `/images/projects/{slug}/`
- Image files: descriptive names (e.g., `figure1_pipeline.png`, `figure3_complete.png`)
- PDFs: keep original filenames in `/files/`

## Common Tasks

### Starting a new project page
```
User provides: PDF filename, desired slug, any specific requests
Agent does:
1. Read PDF metadata and abstract
2. Identify key figures and their pages
3. Extract figures at 300 DPI
4. Show user the extracted images for approval
5. Create project page markdown
6. Update publications.md to featured format
```

### Fixing figure extraction
```
1. Identify correct page number for the figure
2. Use get_text('dict') to find caption/title positions
3. Use get_images() and get_image_info() for embedded image positions
4. Render at 300 DPI with appropriate clip region
5. Show user for verification before updating markdown
```

## Development Commands

```bash
# Start Jekyll server
bundle exec jekyll serve --config _config.dev.yml --livereload

# Python for PDF extraction (pymupdf must be installed)
python -c "import pymupdf; ..."
```

## Questions to Ask User

Before starting a new project page:
- Which PDF should I use? (filename in /files/)
- What slug/URL do you want? (e.g., "fa4gcf")
- Any specific figures or sections to prioritize?
- Is there a GitHub repo for the code?
