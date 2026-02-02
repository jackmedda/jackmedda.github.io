from PIL import Image
import os

def fix_black_bg(img_path):
    img = Image.open(img_path).convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        # If pixel is black (or near black), set to white
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            newData.append((255, 255, 255, item[3]))
        else:
            newData.append(item)
    img.putdata(newData)
    img = img.convert('RGB')
    img.save(img_path)
    print(f'Fixed: {img_path}')

folder = 'images/projects/improving-fairness-speaker/'
for fname in os.listdir(folder):
    if fname.endswith('.png') and fname.startswith('figure'):
        fix_black_bg(os.path.join(folder, fname))
