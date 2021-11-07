import os 
from pathlib import Path
import glob
import shutil
import csv
import os.path
import operator

dir_path = "/home/bee/tools/bee-client-master/202108_auto/WS/cepco/2021-11-07_08_03_29_output/obj_train_data/" # mix
dir_pathOut = "/home/bee/work/tmp/workroom/00/" #

dir_list = os.listdir(dir_path)
full_size = 0
train = []
dir_list.sort()

for file_name_i in dir_list:
        file_size = os.path.getsize(os.path.join(dir_path,file_name_i))
        file_name = Path(file_name_i).stem
        if file_size == 0 :
                aa = glob.glob(dir_path + file_name + '.*')
                for n in aa:
                        shutil.move(n,dir_pathOut)
        else:
                pass
"""
                print("file_size=",file_size)
                fn, ext = os.path.splitext(file_name_i)
                print("ext=",ext)        
                if ext == ".jpg" :
                        trainLine = "data/obj_train_data/" + file_name + ".jpg"
                        train.append([trainLine])
                        with open( dir_path3 + 'train.txt', 'w') as fout:
                                writer = csv.writer(fout)
                                writer.writerows(train)
                                fout.close


mycsv = csv.reader(open(dir_path3 + 'train.txt'))
result = sorted(mycsv, key=operator.itemgetter(0))
with open(dir_path3 + 'train.txt', "w") as f:
    data = csv.writer(f)
    for r in result:
        data.writerow(r)
"""
