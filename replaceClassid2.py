#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#20211223 copyright BeeKnowledgeDesign

import os
from glob import glob

dirName = "input"
new_dir_path = 'clone_data'
try:
    os.mkdir(new_dir_path)
except:
    pass

print('変更したいクラス番号を入れてください。')
classID1  = input('>> ')
findItem1 = str(classID1 + " ")
print('変更後のクラス番号を入れてください。')
classID2  = input('>> ')
findItem2 = str(classID2 + " ")


def replaceOb(fName,oName,outName,delLine,repLine):
    with open(fName, "r") as input:
        #filename 分離
        with open(outName + "/" + oName, "w") as output: 
            for line in input:
                checkString = line.startswith(delLine)
                if checkString == True:
                    print(line)
                    line = line.replace(delLine, repLine,1)# 最後の数は置換回数
                    output.write(line)
                    
                else:
                    output.write(line)

    input.close()
    output.close()

for file in glob(dirName + '/*.txt'):
    #print(file)
    fileOrg = os.path.split(file)[1]
    replaceOb(file,fileOrg,new_dir_path,findItem1,findItem2)
