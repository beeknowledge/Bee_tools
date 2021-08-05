import os
import glob
from PIL import Image

dst_dir = 'small'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('temp/*')

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))
    except OSError as e:
        pass
