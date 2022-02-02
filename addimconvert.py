#使い方　Imagesフォルダを作成。その中にjpgファイルを配置
#プログラム実行　出力画像の大きさを設定　角度を設定するとタイル状の画像が出力され、結果をYolo座標形式で出力する。

import math
import cv2
import numpy as np
import sys
import csv
import os
import glob


wsize = int(input("Enter width_size:"))
hsize = int(input("Enter height_size:"))
#wsize,hsize:ベースとなる解像度の幅と高さ

if wsize <= 0 or hsize <= 0:
    print("Error:Invalid number")
    sys.exit()
#無効な数字

answer = str(input("Do you convert the Images_folder?(y,n):"))

if answer == "n" or answer == "no":

    img = str(input("Enter File_name:"))

    im = cv2.imread(img)

    h, w, _ = im.shape
    #w,h:読み込んだ画像の幅と高さ

    rotation = int(input("Enter an angle:"))
    #時計回りに回転させたい角度

    if not (rotation == 0 or rotation == 90 or rotation == 180 or rotation == 270):
        print("Error:Invalid number")
        sys.exit()
    #無効な数字

    if rotation == 90:
        im = cv2.rotate(im,cv2.ROTATE_90_CLOCKWISE)

    if rotation == 180:
        im = cv2.rotate(im,cv2.ROTATE_180)

    if rotation == 270:
        im = cv2.rotate(im,cv2.ROTATE_90_COUNTERCLOCKWISE)

    #各角度による画像の置換

    if rotation == 90 or 270:
        w, h =h, w

    w_return = math.floor(wsize/w)
    h_return = math.floor(hsize/h)
    #縦横に並べられる画像の数
    if w_return == 0 or h_return == 0:
        print("Error:Cannot be placed {im}")
        sys.exit()
    #配置可能な場所がない
    
    def concat_tile(im_list_2d):
        return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])
    #タイル状に画像を並べる関数
    im_tile = concat_tile([[im]*w_return for i in range(h_return)])
    root, ext = os.path.splitext(img)
    basename = os.path.basename(root)
    cv2.imwrite(os.path.join(basename + '_addimconvert' + ext), im_tile)
    


    #txtファイル作成
    k = 0
    x = w/2
    y = h/2
    classid = [0]
    classCounter = str(classid[0])
    annotation = []
    while k < h_return:
        l =0
        while l < w_return:
            hhh = str(classid[0]) + ' ' + str('{:.06f}'.format(round(x/wsize, 6))) + ' ' + str('{:.06f}'.format(round(y/hsize, 6))) + ' ' + str('{:.06f}'.format(round(0.95*w/wsize, 6))) + ' ' + str('{:.06f}'.format(round(0.95*h/hsize, 6)))
            annotation.append([hhh])
            x += w
            l +=1
       
        k += 1
        x = w/2
        y += h

        with open(os.path.join(basename + '_addimconvert.txt' ) , 'w') as fout:
            writer = csv.writer(fout)
            writer.writerows(annotation)
            fout.close
            
elif answer == "y" or answer == "yes":

    rotation = int(input("Enter an angle:"))
    #時計回りに回転させたい角度

    if not (rotation == 0 or rotation == 90 or rotation == 180 or rotation == 270):
        print("Error:Invalid number")
        sys.exit()
    #無効な数字

    dst_dir = './addimconvert_Images'
    
    os.makedirs(dst_dir, exist_ok = True)
    
    files = glob.glob('./Images/*.jpg')

    txt_dir = './addimconvert_Texts'
    
    os.makedirs(txt_dir, exist_ok = True)
    
    for f in files:
         
        im = cv2.imread(f)

        h, w, _ = im.shape
        #w,h:読み込んだ画像の幅と高さ

        if rotation == 90:
            im = cv2.rotate(im,cv2.ROTATE_90_CLOCKWISE)
        if rotation == 180:
            im = cv2.rotate(im,cv2.ROTATE_180)
        if rotation == 270:
            im = cv2.rotate(im,cv2.ROTATE_90_COUNTERCLOCKWISE)

        #各角度による画像の置換

        if rotation == 90 or 270:
            w, h =h, w

        w_return = math.floor(wsize/w)
        h_return = math.floor(hsize/h)
        #縦横に並べられる画像の数
        
        if w_return == 0 or h_return == 0:
            print("Error:Cannot be placed {im}")
            sys.exit()
        #配置可能な場所がない
    
        def concat_tile(im_list_2d):
            return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])
        #タイル状に画像を並べる関数
        
        im_tile = concat_tile([[im]*w_return for i in range(h_return)])
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        cv2.imwrite(os.path.join(dst_dir, basename + '_addimconvert' + ext), im_tile)


        #txtファイル作成            
        k = 0
        x = w/2
        y = h/2
        classid = [0]
        classCounter = str(classid[0])
        annotation = []
        while k < h_return:
            l =0
            while l < w_return:
                hhh = str(classid[0]) + ' ' + str('{:.06f}'.format(round(x/wsize, 6))) + ' ' + str('{:.06f}'.format(round(y/hsize, 6))) + ' ' + str('{:.06f}'.format(round(0.95*w/wsize, 6))) + ' ' + str('{:.06f}'.format(round(0.95*h/hsize, 6)))
                annotation.append([hhh])
                x += w
                l +=1
       
            k += 1
            x = w/2
            y += h

            with open(os.path.join(txt_dir, basename + '_addimconvert.txt' ) , 'w') as fout:
                writer = csv.writer(fout)
                writer.writerows(annotation)
                fout.close
                

else:
    print("Error:Invalid answer")










