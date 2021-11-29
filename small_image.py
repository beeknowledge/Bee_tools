import os
import glob
import PIL.Image
import random
import string

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from functools import partial

def GetRandomStr(num):
    # 英数字をすべて取得
    dat = string.digits + string.ascii_lowercase + string.ascii_uppercase

    # 英数字からランダムに取得
    return ''.join([random.choice(dat) for i in range(num)])

def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))


    
def read_dir_clicked(entry_form):
    # iDir = os.path.abspath(os.path.dirname(__file__))
    iDir = os.path.abspath(os.path.dirname(read_base_dir))
    filepath = filedialog.askdirectory(initialdir = iDir)
    entry_form.set(filepath)

def read_file_clicked_with_label_set(entry_form):
    iDir = os.path.abspath(os.path.dirname(read_base_dir))
    filepath = filedialog.askopenfilename(initialdir = iDir)
    entry_form.set(filepath)
    label_setting(filepath)

def changeImage(dirI,dst_dir):
    files = glob.glob(dirI+'/*')
    print(files)
    Numname = GetRandomStr(3)
    if file6_entry.get().isdigit()== True :
        for f in files:
            try:
                img = PIL.Image.open(f)
                root, ext_t = os.path.splitext(f)
                ext = ".jpg"
                basename = os.path.basename(root)
                dst = scale_to_width(img, int(file6_entry.get()))
                
                #img_resize.save(os.path.join(dst_dir, basename + '_half' + ext), optimize=True , quality=90)
                dst.save(os.path.join(dst_dir, Numname + basename + '_half' + ext), optimize=True , quality=95)
            except OSError as e:
                pass
    else:
        messagebox.showinfo('エラーメッセージ', u'サイズは半角小文字で指定してください。')
        

# start_btnクリック時の処理(Startボタン)
def start_btn_clicked():
    try:
        inDir = file4.get()
        outDir = file5.get()

        if not os.path.exists(inDir) or inDir == "":
            messagebox.showinfo('エラーメッセージ', u'読込先フォルダのパスを確認してください')
            return
        elif not os.path.exists(outDir) or outDir == "":
            messagebox.showinfo('エラーメッセージ', u'保存先フォルダのパスを確認してください')
            return
        basename_without_ext = os.path.splitext(os.path.basename(inDir))
        print(basename_without_ext)
        changeImage(inDir,outDir)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #config setting
    read_base_dir = "./"
    
    # rootの作成
    root = Tk()
    root.title("画像のリサイズ")#add 20210814
    root.resizable(False, False)
    root.geometry('+%d+%d'%(50,50))

    #隠しファイルの非表示設定
    try:
        # call a dummy dialog with an impossible option to initialize the file
        # dialog without really getting a dialog window; this will throw a
        # TclError, so we need a try...except :
        try:
            root.tk.call('tk_getOpenFile', '-foobarbaz')
        except TclError:
            pass
        # now set the magic variables accordingly
        root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
    except:
        pass   

    #Frame_wrapper
    frame_wrapper = ttk.Frame(root, padding=(10,20))
    frame_wrapper.grid()


    # Frame1
    frame1 = ttk.Frame(frame_wrapper, padding=(10,15))
    frame1.grid()


    # input dir
    s4 = StringVar()
    s4.set('読込先:')
    label4 = ttk.Label(frame1, textvariable=s4)
    label4.grid(row=4, column=0, padx=5, pady=5)

    file4 = StringVar()
    file4_entry = ttk.Entry(frame1, textvariable=file4, width=60)
    file4_entry.grid(row=4, column=1, padx=5, pady=5)

    read_path_btn = ttk.Button(frame1, text=u'参照', command=partial(read_dir_clicked, file4))
    read_path_btn.grid(row=4, column=2, padx=5, pady=5)

    # output dir
    s5 = StringVar()
    s5.set('保存先:')
    label5 = ttk.Label(frame1, textvariable=s5)
    label5.grid(row=5, column=0, padx=5, pady=5)

    file5 = StringVar()
    file5_entry = ttk.Entry(frame1, textvariable=file5, width=60)
    file5_entry.grid(row=5, column=1, padx=5, pady=5)

    read_path_btn = ttk.Button(frame1, text=u'参照', command=partial(read_dir_clicked, file5))
    read_path_btn.grid(row=5, column=2, padx=5, pady=5)

    s6 = StringVar()
    s6.set('width:')
    label6 = ttk.Label(frame1, textvariable=s6)
    label6.grid(row=6, column=0, padx=5, pady=5)
    file6_entry = tkinter.Entry(width=20)
    file6_entry.place(x=80, y=120)
    file6_entry.insert(0, 1000)

    # Frame3 for start button
    frame3 = ttk.Frame(frame_wrapper, padding=(10,10))
    frame3.grid()
    
    start_btn = ttk.Button(frame3, text='実行', command=start_btn_clicked)
    start_btn.grid(row=8, column=1,pady=10)# add 20210907



    root.mainloop()    
