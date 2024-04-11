import tkinter as tk
import random
import csv
import datetime

def generate_password():
    # パスワードを生成する関数
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(10):
        password += random.choice(characters)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_data():
    # 入力データとパスワードをCSVファイルに保存する関数
    name = name_entry.get()
    id = id_entry.get()
    data = data_entry.get()
    password = password_entry.get()
    date = datetime.date.today().strftime('%Y-%m-%d')
    with open('output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, name, id, data, password])
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Password Generator')

# 氏名の入力フィールド
name_label = tk.Label(root, text='氏名')
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# IDの入力フィールド
id_label = tk.Label(root, text='ID')
id_label.grid(row=1, column=0, padx=5, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1, padx=5, pady=5)

# 入力リストの入力フィールド
data_label = tk.Label(root, text='入力リスト（コンマ区切り）')
data_label.grid(row=2, column=0, padx=5, pady=5)
data_entry = tk.Entry(root)
data_entry.grid(row=2, column=1, padx=5, pady=5)

# パスワード生成ボタン
password_button = tk.Button(root, text='パスワード生成', command=generate_password)
password_button.grid(row=3, column=0, padx=5, pady=5)

# パスワード表示フィールド
password_label = tk.Label(root, text='パスワード')
password_label.grid(row=3, column=1, padx=5, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=3, column=2, padx=5, pady=5)

# 保存ボタン
save_button = tk.Button(root, text='保存', command=save_data)
save_button.grid(row=4, column=1, padx=5, pady=5)

# 日付表示ラベル
date_label = tk.Label(root, text=datetime.date.today().strftime('%Y-%m-%d'))
date_label.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
