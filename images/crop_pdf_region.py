#!/usr/bin/env python3
"""
Crop a specific region from a PDF page and save as image.
Useful for extracting figures/diagrams.
"""

import pymupdf as fitz
import sys
from pathlib import Path

def crop_region(pdf_path: str, page_num: int, output_path: str, 
                top_pct: float = 0, bottom_pct: float = 100, 
                left_pct: float = 0, right_pct: float = 100,
                dpi: int = 300):
    """
    Crop a specific region of a PDF page as an image.
    
    Args:
        pdf_path: Path to PDF file
        page_num: Page number (1-indexed)
        output_path: Output image path
        top_pct: Top of crop region (0-100%)
        bottom_pct: Bottom of crop region (0-100%)
        left_pct: Left of crop region (0-100%)
        right_pct: Right of crop region (0-100%)
        dpi: Output resolution
    """
    doc = fitz.open(pdf_path)
    
    if page_num < 1 or page_num > doc.page_count:
        print(f"Error: Page {page_num} is out of range (1-{doc.page_count})")
        return False
    
    page = doc[page_num - 1]
    rect = page.rect
    
    # Calculate crop rectangle from percentages
    width = rect.width
    height = rect.height
    
    crop_rect = fitz.Rect(
        rect.x0 + (left_pct / 100) * width,
        rect.y0 + (top_pct / 100) * height,
        rect.x0 + (right_pct / 100) * width,
        rect.y0 + (bottom_pct / 100) * height
    )
    
    # Render at specified DPI
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=crop_rect)
    
    pix.save(output_path)
    print(f"Cropped region from page {page_num} to {output_path}")
    print(f"Size: {pix.width}x{pix.height}")
    
    doc.close()
    return True

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python crop_pdf_region.py <pdf_path> <page_number> <output_path> [top%] [bottom%] [left%] [right%] [dpi]")
        print("Example: python crop_pdf_region.py paper.pdf 6 figure.png 30 70 10 90 300")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    page_num = int(sys.argv[2])
    output_path = sys.argv[3]
    
    top = float(sys.argv[4]) if len(sys.argv) > 4 else 0
    bottom = float(sys.argv[5]) if len(sys.argv) > 5 else 100
    left = float(sys.argv[6]) if len(sys.argv) > 6 else 0
    right = float(sys.argv[7]) if len(sys.argv) > 7 else 100
    dpi = int(sys.argv[8]) if len(sys.argv) > 8 else 300
    
    crop_region(pdf_path, page_num, output_path, top, bottom, left, right, dpi)
