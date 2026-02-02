import pymupdf

def extract_subplot(pdf_path, page_num, rect, out_path, scale=150/72):
    doc = pymupdf.open(pdf_path)
    page = doc[page_num]
    mat = pymupdf.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, clip=pymupdf.Rect(*rect))
    pix.save(out_path)
    print(f'Saved {out_path}: {pix.width}x{pix.height}')
    doc.close()

pdf = 'files/improving_fairness_speaker_3393822.3432325.pdf'
page = 8
# Adjusted bounding boxes for right subplots (wider)
right_subplots = [
    (580, 60, 1090, 420, 'figure2_subplot2.png'),
    (580, 440, 1090, 800, 'figure2_subplot4.png'),
    (580, 820, 1090, 1180, 'figure3_subplot2.png'),
]
for x0, y0, x1, y1, fname in right_subplots:
    extract_subplot(pdf, page, (x0, y0, x1, y1), f'images/projects/improving-fairness-speaker/{fname}')
