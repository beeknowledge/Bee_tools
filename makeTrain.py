import os 
from pathlib import Path
import glob
import shutil
import csv
import os.path
import operator

dir_path = "/home/bee/tools/bee-client-master/202108_auto/WS/cepco/2021-11-07_08_03_29_output/obj_train_data/" # mix
dir_pathOut = "/home/bee/tools/bee-client-master/202108_auto/WS/cepco/2021-11-07_08_03_29_output/" #

dir_list = os.listdir(dir_path)
full_size = 0
train = []
dir_list.sort()
for file_name_i in dir_list:
        file_name = Path(file_name_i).stem

        fn, ext = os.path.splitext(file_name_i)
        print("ext=",ext)        
        if ext == ".jpg" :
                trainLine = "data/obj_train_data/" + file_name + ".jpg"
                train.append([trainLine])
                with open( dir_pathOut + 'train.txt', 'w') as fout:
                        writer = csv.writer(fout)
                        writer.writerows(train)
                        fout.close


mycsv = csv.reader(open(dir_pathOut + 'train.txt'))
result = sorted(mycsv, key=operator.itemgetter(0))
with open(dir_pathOut + 'train.txt', "w") as f:
    data = csv.writer(f)
    for r in result:
        data.writerow(r)

