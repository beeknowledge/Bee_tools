import os
import shutil

# ===== 設定 =====
# 作業ディレクトリ（txt と jpg ファイルが存在するディレクトリ）のパスを指定してください
source_dir = r'obj_train_data'  # 例: r'C:\Users\YourName\Documents\files'
# 出力先ディレクトリ（存在しなければ自動で作成します）
output_dir = os.path.join(source_dir, 'out')

# ===== 出力先ディレクトリの準備 =====
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f'Created output directory: {output_dir}')

# ===== ファイルの処理 =====
# source_dir 内のすべてのファイルをチェック
for filename in os.listdir(source_dir):
    # ファイルが txt ファイルかどうかチェック（大文字小文字の違いも考慮）
    if filename.lower().endswith('.txt'):
        txt_path = os.path.join(source_dir, filename)
        # txt ファイルを開き、先頭2文字を読み込む
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                header = file.read(2)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        # 先頭が "13" であれば、txt と対応する jpg を出力先にコピーする
        if header == '12':
            print(f"{filename} の先頭が '12' です。ファイルをコピーします。")
            # txt ファイルのコピー
            try:
                shutil.copy(txt_path, output_dir)
            except Exception as e:
                print(f"Error copying {filename}: {e}")

            # 対応する jpg ファイルのパスを作成（拡張子以外は同じ）
            base_name = os.path.splitext(filename)[0]
            jpg_filename = base_name + '.jpg'
            jpg_path = os.path.join(source_dir, jpg_filename)

            # jpg ファイルが存在するか確認してコピー
            if os.path.exists(jpg_path):
                try:
                    shutil.copy(jpg_path, output_dir)
                except Exception as e:
                    print(f"Error copying {jpg_filename}: {e}")
            else:
                print(f"Warning: {filename} に対応する jpg ファイル ({jpg_filename}) が見つかりません。")
