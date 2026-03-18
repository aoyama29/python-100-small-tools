import random

# 1. コンピュータが1〜100の間で数字を1つ決める
answer = random.randint(1, 100)
count = 0  # 何回で当たったか数える用

print("=== 数当てゲーム（1〜100） ===")

# 2. 当たるまで繰り返す（while文）
while True:
    guess = int(input("数字を予想して入力してね: "))
    count += 1  # 試行回数を1増やす

    if guess == answer:
        print(f"正解！ {count}回目で当たりました！ ✨")
        break  # 正解したので繰り返しを終了する
    elif guess < answer:
        print("もっと【大きい】ですよ！ ↑")
    else:
        print("もっと【小さい】ですよ！ ↓")
