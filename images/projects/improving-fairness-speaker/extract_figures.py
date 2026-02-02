import pymupdf
import io
from PIL import Image

doc = pymupdf.open('files/improving_fairness_speaker_3393822.3432325.pdf')
xrefs = [142, 189, 200]
names = ['figure1_results.png', 'figure2_results.png', 'figure3_results.png']
for xref, name in zip(xrefs, names):
    base_image = doc.extract_image(xref)
    img = Image.open(io.BytesIO(base_image['image']))
    img.save(f'images/projects/improving-fairness-speaker/{name}', 'PNG')
    print(f'Saved {name}: {img.size}')
