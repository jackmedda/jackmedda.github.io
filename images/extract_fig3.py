import pymupdf as fitz
import os

pdf_path = r'c:\Users\jackm\PythonProjects\jackmedda.github.io\files\fair_augmentation_recsys_3640457.3688064.pdf'
output_dir = r'c:\Users\jackm\PythonProjects\jackmedda.github.io\images\projects\fa4gcf'

doc = fitz.open(pdf_path)
page = doc[8]  # Page 9

# Get text to understand layout
print("=== Page 9 text blocks ===")
blocks = page.get_text('dict')['blocks']
for block in blocks:
    if 'lines' in block:
        for line in block['lines']:
            for span in line['spans']:
                text = span['text'].strip()
                if text and len(text) > 2:
                    y = span['bbox'][1]
                    print(f"y={y:.0f}: {text[:60]}")

# Now extract Figure 3 with good coordinates
# Based on the PDF structure, Figure 3 should be near the top of page 9
dpi = 300
mat = fitz.Matrix(dpi/72, dpi/72)

# Try different regions to find the figure
# Looking at the text, the figure should be between y~80 and y~350
clip_rect = fitz.Rect(30, 65, 580, 360)
pix = page.get_pixmap(matrix=mat, clip=clip_rect)
pix.save(os.path.join(output_dir, 'figure3_v2.png'))
print(f"\nSaved figure3_v2.png: {pix.width}x{pix.height}")

# Also try extracting individual subplots
# The 2x2 grid with titles:
# Top-left: NCL, ΨU varies | Top-right: NCL, ΨI varies  
# Bottom-left: SGL, ΨU varies | Bottom-right: SGL, ΨI varies

# Approximate subplot positions (in points)
# Each subplot is roughly 250 points wide
half_width = 290
subplot_height = 135

# Top row y range: ~90 to ~225
# Bottom row y range: ~225 to ~360

y_top = 90
y_mid = 220
y_bot = 355
x_left = 45
x_mid = 310
x_right = 575

subplots = [
    ('fig3_ncl_psi_u.png', fitz.Rect(x_left, y_top, x_mid, y_mid)),
    ('fig3_ncl_psi_i.png', fitz.Rect(x_mid, y_top, x_right, y_mid)),
    ('fig3_sgl_psi_u.png', fitz.Rect(x_left, y_mid, x_mid, y_bot)),
    ('fig3_sgl_psi_i.png', fitz.Rect(x_mid, y_mid, x_right, y_bot)),
]

for name, rect in subplots:
    pix = page.get_pixmap(matrix=mat, clip=rect)
    pix.save(os.path.join(output_dir, name))
    print(f"Saved {name}: {pix.width}x{pix.height}")
