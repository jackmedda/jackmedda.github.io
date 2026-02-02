import pymupdf
from PIL import Image

pdf = 'files/improving_fairness_speaker_3393822.3432325.pdf'
doc = pymupdf.open(pdf)
page = doc[8]
scale = 150/72
mat = pymupdf.Matrix(scale, scale)
clip = pymupdf.Rect(0, 0, 1110, 420)  # Start from very top, full width
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_top_half_wide.png')

img = Image.open('images/projects/improving-fairness-speaker/figure2_top_half_wide.png')
width, height = img.size
center = width // 2
portion = int(width * 0.28)
left = img.crop((center - portion, 0, center, height))
right = img.crop((center, 0, center + portion, height))
left.save('images/projects/improving-fairness-speaker/figure2_subplot1_wide.png')
right.save('images/projects/improving-fairness-speaker/figure2_subplot2_wide.png')
print(f'Saved left subplot: {left.size}, right subplot: {right.size}')
