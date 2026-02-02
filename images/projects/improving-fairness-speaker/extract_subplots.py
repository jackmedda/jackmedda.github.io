import pymupdf

doc = pymupdf.open('files/improving_fairness_speaker_3393822.3432325.pdf')
page = doc[8]
scale = 300/72
mat = pymupdf.Matrix(scale, scale)

# Subplot 1 (top left)
clip = pymupdf.Rect(50, 50, 600, 500)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_subplot1.png')
print('Saved subplot1:', pix.width, pix.height)
# Subplot 2 (top right)
clip = pymupdf.Rect(650, 50, 1150, 500)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_subplot2.png')
print('Saved subplot2:', pix.width, pix.height)
# Subplot 3 (bottom left)
clip = pymupdf.Rect(50, 500, 600, 950)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_subplot3.png')
print('Saved subplot3:', pix.width, pix.height)
# Subplot 4 (bottom right)
clip = pymupdf.Rect(650, 500, 1150, 950)
pix = page.get_pixmap(matrix=mat, clip=clip)
pix.save('images/projects/improving-fairness-speaker/figure2_subplot4.png')
print('Saved subplot4:', pix.width, pix.height)
