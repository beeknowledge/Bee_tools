import os
import glob
from PIL import Image
import random
import string

def GetRandomStr(num):
    # 英数字をすべて取得
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase

    # 英数字からランダムに取得
    return ''.join([random.choice(dat) for i in range(num)])

dst_dir = 'tmp'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('all/*')

Numname = GetRandomStr(3)

def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))

for f in files:
    try:
        img = Image.open(f)
        #img_resize = img.resize((img.width // 1, img.height // 1))
        root, ext_t = os.path.splitext(f)
        ext = ".jpg"
        basename = os.path.basename(root)
        dst = scale_to_width(img, 2000)
        
        #img_resize.save(os.path.join(dst_dir, basename + '_half' + ext), optimize=True , quality=90)
        dst.save(os.path.join(dst_dir, Numname + basename + '_half' + ext), optimize=True , quality=95)
    except OSError as e:
        pass
