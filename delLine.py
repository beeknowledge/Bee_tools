# delLine.py

inputFile = "tes.txt"     # 読み込みファイル
outputFile = "output.txt"   # 書き込みファイル

NGWord = ["data_ "]    

for line in open(inputFile):
    # 行中にNGWordを含むか判別
    for i in NGWord:
        if i in line:
            break
        else:
            # 書き込みファイルの末尾にその行を追加
            with open(outputFile, mode='a') as f:
                 f.write(line)

