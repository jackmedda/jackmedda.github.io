#!/usr/bin/env python3
"""
Render a specific PDF page as an image.
Useful for capturing vector graphics like Kiviat/radar diagrams.
"""

import pymupdf as fitz
import sys
from pathlib import Path

def render_page(pdf_path: str, page_num: int, output_path: str, dpi: int = 200):
    """Render a specific page of a PDF as a PNG image."""
    doc = fitz.open(pdf_path)
    
    if page_num < 1 or page_num > doc.page_count:
        print(f"Error: Page {page_num} is out of range (1-{doc.page_count})")
        return False
    
    page = doc[page_num - 1]  # 0-indexed
    
    # Render at specified DPI
    zoom = dpi / 72  # 72 is the default PDF resolution
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    # Save as PNG
    pix.save(output_path)
    print(f"Rendered page {page_num} to {output_path}")
    print(f"Size: {pix.width}x{pix.height}")
    
    doc.close()
    return True

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python extract_page_render.py <pdf_path> <page_number> <output_path> [dpi]")
        print("Example: python extract_page_render.py paper.pdf 6 page6.png 300")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    page_num = int(sys.argv[2])
    output_path = sys.argv[3]
    dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    
    render_page(pdf_path, page_num, output_path, dpi)
