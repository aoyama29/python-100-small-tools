import os

# 1. 操作したいフォルダのパスを指定
# (Windowsの場合は r"C:\Users\名前\Desktop\practice" のように書きます)
folder_path = input("フォルダのパスを入力してください: ")

# 2. フォルダ内のファイル一覧を取得
files = os.listdir(folder_path)

print(f"--- {folder_path} 内のファイルを変更します ---")

# 3. 一つずつ名前を変更する
for i, filename in enumerate(files):
    # 元のファイルパス
    old_path = os.path.join(folder_path, filename)
    
    # 新しい名前を作成（例：001_元の名前）
    new_name = f"{i+1:03}_{filename}"
    new_path = os.path.join(folder_path, new_name)
    
    # 実際に名前を変更
    os.rename(old_path, new_path)
    print(f"変更前: {filename} -> 変更後: {new_name}")

print("\nすべての変更が完了しました！")
