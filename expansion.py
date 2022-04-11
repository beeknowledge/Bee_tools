import math
import cv2
import numpy as np
import sys
import csv
import os
import glob
import tkinter
from os import listdir
from tkinter import filedialog
from tkinter import messagebox
import datetime
import shutil

def folder_select1():
    idir = '.'
    fld1 = filedialog.askdirectory(initialdir = idir)
    input_box1.delete(0, tkinter.END)
    input_box1.insert(tkinter.END, fld1)
    return fld1
def folder_select2():
    idir = '.'
    fld2 = filedialog.askdirectory(initialdir = idir)
    input_box2.delete(0, tkinter.END)
    input_box2.insert(tkinter.END, fld2)
    return fld2

def expansion():
    traintext = []
    in_folder = str(input_box1.get())
    if not in_folder:
        messagebox.showerror("エラー", "入力に漏れがあります")
        sys.exit()
    elif in_folder.isspace() == True:
        messagebox.showerror("エラー", "入力に漏れがあります")
        sys.exit()
    else:
        in_folder_ad = in_folder

    ex_folder = str(input_box2.get())
    if not ex_folder:
        messagebox.showerror("エラー", "入力に漏れがあります")
        sys.exit()
    elif ex_folder.isspace() == True:
        messagebox.showerror("エラー", "入力に漏れがあります")
        sys.exit()
    else:
        ex_folder_ad = ex_folder
        
    #wsize,hsize:ベースとなる解像度の幅と高さ
    wsize = input_box3.get()
    hsize = input_box4.get()
    #無効な数字
    if wsize.isdecimal() == False:
        messagebox.showerror("エラー", "解像度は整数で入力してください")
        sys.exit()
    if hsize.isdecimal() == False:
        messagebox.showerror("エラー", "解像度は整数で入力してください")
        sys.exit()
    
    wsize = int(wsize)
    hsize = int(hsize)

    cls = "0"
    if input_box5.get():
        cls = str(input_box5.get())
    if cls.isdecimal() == False:
        messagebox.showerror("エラー", "クラス番号は整数で入力してください")
        sys.exit()

    cls = int(cls)

    rot = "0"
    if input_box6.get():
        rot = str(input_box6.get())
    if rot.isdecimal() == False:
        messagebox.showerror("エラー", "0, 90, 180, 270を整数で入力してください")
        sys.exit()
        
    rot = int(rot)

    if not (rot == 0 or rot == 90 or rot == 180 or rot == 270):
            messagebox.showerror("エラー", "0, 90, 180, 270を整数で入力してください")
            sys.exit()

    siz = "100"
    if input_box7.get():
        siz = str(input_box7.get())
    if siz.isdecimal() == False:
        messagebox.showerror("エラー", "拡大・縮小率は整数で入力してください")
        sys.exit()

    siz = int(siz)

    dst_dir = ex_folder_ad + '/expansion_Images'
        
    os.makedirs(dst_dir, exist_ok = True)
        
    files = glob.glob(in_folder_ad + '/*.jpg')

    if len(files) == 0:
        messagebox.showerror("エラー", "無効なファイル名です")

    txt_dir = ex_folder_ad + '/obj_train_data'
        
    os.makedirs(txt_dir, exist_ok = True)
        
    for f in files:
             
        im = cv2.imread(f)
        #w,h:読み込んだ画像の幅と高さ
        h, w, _ = im.shape

        #各角度による画像の置換
        rotname = ""
        if rot == 90:
            im = cv2.rotate(im,cv2.ROTATE_90_CLOCKWISE)
            rotname = "_90rot"
        if rot == 180:
            im = cv2.rotate(im,cv2.ROTATE_180)
            rotname = "_180rot"
        if rot == 270:
            im = cv2.rotate(im,cv2.ROTATE_90_COUNTERCLOCKWISE)
            rotname = "_270rot"
            
        if rot == 90 or rot == 270:
            w, h = h, w
        #拡大・縮小による画像の置換
        sizname = ""
        if siz != 100:
            ratio = siz/100
            im = cv2.resize(im, dsize = None, fx = ratio, fy = ratio, interpolation = cv2.INTER_LANCZOS4)
            w, h = w*ratio, h*ratio
            sizname = "_" + str(siz) + "exp"

        #縦横に並べられる画像の数
        w_return = math.floor(wsize/w)
        h_return = math.floor(hsize/h)
        #配置可能な場所がない    
        if w_return == 0 or h_return == 0:
            messagebox.showerror("エラー", "配置可能な場所がありません")
            sys.exit()
        #タイル状に画像を並べる関数
        def concat_tile(im_list_2d):
            return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])
            
        im_tile = concat_tile([[im]*w_return for i in range(h_return)])
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        cv2.imwrite(os.path.join(dst_dir, basename + rotname + sizname + ext), im_tile)


        #txtファイル作成            
        k = 0
        x = w/2
        y = h/2
        annotation = []
        traintext.append(basename + rotname + sizname + '.txt')


        while k < h_return:
                l =0
                while l < w_return:
                    hhh = str(cls) + ' ' + str('{:.06f}'.format(round(x/w/w_return, 6))) + ' ' + str('{:.06f}'.format(round(y/h/h_return, 6))) + ' ' + str('{:.06f}'.format(round(0.95*w/w/w_return, 6))) + ' ' + str('{:.06f}'.format(round(0.95*h/h/h_return, 6)))
                    annotation.append([hhh])
                    x += w
                    l +=1
           
                k += 1
                x = w/2
                y += h

                with open(os.path.join(txt_dir, basename + rotname + sizname + '.txt' ) , 'w') as fout:
                    writer = csv.writer(fout)
                    writer.writerows(annotation)
                    fout.close

    with open(ex_folder_ad + '/' + 'train.txt', 'w') as f_new:
        for n in traintext:
            n= "data/obj_train_data/" + n
            print(n)
            f_new.write("%s\n" % n)
            #f_new.write(n)
    dt = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    shutil.make_archive(dt + '_output', 'zip', root_dir=ex_folder_ad)
    messagebox.showinfo("確認","出力が完了しました")
    #print(traintext)

win = tkinter.Tk()
win.title("教師データ拡張ツール")
win.geometry("600x380")
#入力欄
input_box1 = tkinter.Entry(width = 30)
input_box1.place(x = 140, y = 30)
input_box2 = tkinter.Entry(width = 30)
input_box2.place(x = 140, y = 80)
input_box3 = tkinter.Entry(width = 8)
input_box3.place(x = 170, y = 130)
input_box4 = tkinter.Entry(width = 8)
input_box4.place(x = 270, y = 130)
input_box5 = tkinter.Entry(width = 8)
input_box5.place(x = 140, y = 180)
input_box6 = tkinter.Entry(width = 8)
input_box6.place(x = 140, y = 230)
input_box7 = tkinter.Entry(width = 8)
input_box7.place(x = 140, y = 280)
#ラベル
input_label1 = tkinter.Label(text = "入力 (フォルダ)")
input_label1.place(x = 20, y = 30)
input_label2 = tkinter.Label(text = "出力 (フォルダ)")
input_label2.place(x = 20, y = 80)
input_label3 = tkinter.Label(text = "出力解像度(幅×高さ)")
input_label3.place(x = 10, y = 130)
input_label5 = tkinter.Label(text = "クラス番号")
input_label5.place(x = 30, y = 180)
input_label6 = tkinter.Label(text = "回転角度")
input_label6.place(x = 36, y = 230)
input_label7 = tkinter.Label(text = "拡大・縮小 (%)")
input_label7.place(x = 20, y = 280)
#ボタン
button_1 = tkinter.Button(text = "参照", command = folder_select1)
button_1.place(x = 450, y = 26)
button_2 = tkinter.Button(text = "参照", command = folder_select2)
button_2.place(x = 450, y = 76)
button_3 = tkinter.Button(text = "実行", command = expansion)
button_3.place(x = 200, y = 330)

win.mainloop()
                













