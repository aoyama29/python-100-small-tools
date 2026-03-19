# --- 006. CLI TODOリスト ---

todos = []  # タスクを保存する空のリスト

while True:
    print("\n--- 現在のTODOリスト ---")
    if not todos:
        print("（タスクはありません）")
    else:
        for i, task in enumerate(todos):
            print(f"{i + 1}: {task}")

    print("\n操作を選んでください (1:追加, 2:削除, 3:終了)")
    choice = input("> ")

    if choice == "1":
        new_task = input("追加するタスクを入力: ")
        todos.append(new_task)  # リストに要素を追加
        print("追加しました！")
        
    elif choice == "2":
        if not todos:
            print("削除するタスクがありません。")
            continue
        num = int(input("削除する番号を入力: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)  # 指定した番号の要素を削除
            print(f"「{removed}」を削除しました。")
        else:
            print("無効な番号です。")
            
    elif choice == "3":
        print("アプリを終了します。お疲れ様でした！")
        break
    else:
        print("1〜3の数字を入力してください。")
