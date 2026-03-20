# --- 007. 文字数カウント ---

print("--- 文字数カウントツール ---")
print("カウントしたい文章を入力してください（Enterで確定）:")

# ユーザーから文章を入力してもらう
text = input("> ")

# 文字数を計算する
total_chars = len(text)
# 空白（スペースや改行）を除いた文字数を計算する
no_space_chars = len(text.replace(" ", "").replace("　", "").replace("\n", ""))

print("-" * 20)
print(f"全体の文字数: {total_chars}")
print(f"空白を除いた文字数: {no_space_chars}")
print("-" * 20)
