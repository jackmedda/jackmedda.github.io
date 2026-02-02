import pymupdf
from PIL import Image
import io

# Render the full top half of the page
pdf = 'files/improving_fairness_speaker_3393822.3432325.pdf'
doc = pymupdf.open(pdf)
page = doc[8]
scale = 150/72
mat = pymupdf.Matrix(scale, scale)
clip = pymupdf.Rect(60, 60, 1110, 420)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_top_half.png')

# Now crop the right subplot using PIL
img = Image.open('images/projects/improving-fairness-speaker/figure2_top_half.png')
width, height = img.size
# Assume left and right are equal width
mid = width // 2
right = img.crop((mid, 0, width, height))
right.save('images/projects/improving-fairness-speaker/figure2_subplot2_pil.png')
print(f'Saved right subplot: {right.size}')
