import random  # ランダムな機能を使うための準備

print("--- 今日の運勢占い ---")

# 運勢のリストを作成
fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

# リストの中から1つをランダムに選ぶ
result = random.choice(fortunes)

print("あなたの今日の運勢は..." + result + " です！")

# 選ばれた結果によって、一言コメントを変える（条件分岐）
if result == "大吉":
    print("最高の一日になりますね！")
elif result == "凶":
    print("忘れ物に気をつけて、慎重に過ごしましょう。")
else:
    print("今日という日を大切に！")
