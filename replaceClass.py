import os 
from pathlib import Path
import glob
import shutil
import csv
import pandas as pd
#filename = 'train.txt'

with open('train.txt',  encoding='utf-8') as f:
    data_lines = f.read()

# 文字列置換
data_lines = data_lines.replace("obj", "Google マップ ")

# 同じファイル名で保存
with open('train2.txt', mode="w",  encoding='utf-8') as f:
    f.write(data_lines)

