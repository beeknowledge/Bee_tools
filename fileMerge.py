import os
import csv
import glob
csv_file = 'train.txt'
file_list = []
name_list = []


file_list = glob.glob("/media/bee/DATA/yolo202108/merge/ann/*.txt")
for fl in file_list:
     basename = os.path.basename(fl)
     print(basename)
     name_list.append("data/obj_train_data/" + basename)


with open(csv_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    for nl in name_list:
         
         print(nl)
         
         csv_writer.writerow([nl])

