import random

print("=== じゃんけんゲーム開始！ ===")
print("0: グー, 1: チョキ, 2: パー")

# 1. プレイヤーの入力を数字で受け取る
player_input = input("出す手を選んでね（0, 1, 2）: ")
player_hand = int(player_input)

# 2. コンピュータの手をランダムに決める
hands = ["グー", "チョキ", "パー"]
computer_hand = random.randint(0, 2)

print(f"あなた: {hands[player_hand]}")
print(f"コンピュータ: {hands[computer_hand]}")

# 3. 勝敗判定（ここが腕の見せ所！）
if player_hand == computer_hand:
    print("結果: あいこです！")
elif (player_hand == 0 and computer_hand == 1) or \
     (player_hand == 1 and computer_hand == 2) or \
     (player_hand == 2 and computer_hand == 0):
    print("結果: あなたの勝ち！ ✨")
else:
    print("結果: あなたの負け... 😭")
