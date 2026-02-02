import pymupdf
from PIL import Image

# Render the full top half of the page
pdf = 'files/improving_fairness_speaker_3393822.3432325.pdf'
doc = pymupdf.open(pdf)
page = doc[8]
scale = 150/72
mat = pymupdf.Matrix(scale, scale)
clip = pymupdf.Rect(60, 60, 1110, 420)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_top_half_full.png')

# Now crop the central region to remove 22% from each side
img = Image.open('images/projects/improving-fairness-speaker/figure2_top_half_full.png')
width, height = img.size
left_margin = int(width * 0.22)
right_margin = int(width * 0.78)
central = img.crop((left_margin, 0, right_margin, height))
central.save('images/projects/improving-fairness-speaker/figure2_top_half_central.png')

# Split into left and right subplots
mid = (right_margin - left_margin) // 2
left_subplot = central.crop((0, 0, mid, height))
right_subplot = central.crop((mid, 0, right_margin - left_margin, height))
left_subplot.save('images/projects/improving-fairness-speaker/figure2_subplot1_central.png')
right_subplot.save('images/projects/improving-fairness-speaker/figure2_subplot2_central.png')
print(f'Saved left subplot: {left_subplot.size}, right subplot: {right_subplot.size}')
