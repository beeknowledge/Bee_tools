import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import ffmpeg
import cv2
import numpy as np


# スピナーコントロール

def spin_changed(*args):
    print('value = %s' % spinval.get())
    if spinval.get().isnumeric():
        s = spinval.get()
        i = int(s)
        spinval.set(i)
        global numcount
        numcount = i
    else:
        spinval.set("0")

# 参照ボタンのイベント
# button1クリック時の処理]
        
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    name = os.path.splitext(os.path.basename(filepath))
    #print(name[0])
    dirname = os.path.dirname(filepath)
    global dirName
    dirName = dirname
    #print(dirName)
    global fname_noextention
    fname_noextention = name[0]
    global dataname
    dataname = filepath
    file1.set(filepath)
    

# button2クリック時の処理
def button2_clicked():
    new_dir_path =dirName + '/' + fname_noextention
    print("path=",new_dir_path)
    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)
    else:
        #messagebox.showinfo('Video to Frame Tool', u'フォルダが存在します。処理を停止します。')
        ret=messagebox.askyesno('確認', 'フォルダが存在します。上書きますか。')
        if ret == False:
            sys.exit()
    m_slice(dataname, new_dir_path,numcount, '.jpg')
    
    messagebox.showinfo('Video to Frame Tool', u'切り出し終了')

def m_slice(path, dir, step, extension):
    movie = cv2.VideoCapture(path)                  # 動画の読み込み
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))   # 動画の全フレーム数を計算
    path_head = dir + '/out_'                       # 静止画のファイル名のヘッダー
    ext_index = np.arange(0, Fs, step)              # 静止画を抽出する間隔
    for i in range(Fs - 1):                         # フレームサイズ分のループを回す
        flag, frame = movie.read()                  # 動画から1フレーム読み込む
        check = i == ext_index                      # 現在のフレーム番号iが、抽出する指標番号と一致するかチェックする
        
        # frameを取得できた(flag=True)時だけ処理を行う
        if flag == True:
            
            # もしi番目のフレームが静止画を抽出するものであれば、ファイル名を付けて保存する
            if True in check:
                # ファイル名は後でフォルダ内で名前でソートした時に連番になるようにする
                if i < 10:
                    path_out = path_head + '0000' + str(i) + extension
                elif i < 100:
                    path_out = path_head + '000' + str(i) + extension
                elif i < 1000:
                    path_out = path_head + '00' + str(i) + extension
                elif i < 10000:
                    path_out = path_head + '0' + str(i) + extension
                else:
                    path_out = path_head + str(i) + extension
                print("path_out",path_out)
                cv2.imwrite(path_out, frame)
            # i番目のフレームが静止画を抽出しないものであれば、何も処理をしない
            else:
                pass
        else:
            pass
    return


if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('Video to Frame Tool')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # Startボタンの作成
    button2 = ttk.Button(frame2, text='Start', command=button2_clicked)
    button2.pack(side=LEFT)

    # Cancelボタンの作成
    button3 = ttk.Button(frame2, text='Cancel', command=quit)
    button3.pack(side=LEFT)

    spinval = StringVar()
    spinval.trace("w", spin_changed)
    
    sp = Spinbox(
        frame1,
        textvariable=spinval,
        from_=15,
        to=500)
    sp.grid(row=0, column=0, sticky=(N, W))

    root.mainloop()
