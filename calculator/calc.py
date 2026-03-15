# --- 002. 四則演算電卓 ---

print("数字を入力して計算してみよう！")

# ユーザーからの入力を受け取る
num1 = input("1つ目の数字: ")
num2 = input("2つ目の数字: ")

# inputで受け取った「文字」を「計算できる整数」に変える
a = int(num1)
b = int(num2)

# 計算結果を変数に入れる
add = a + b
sub = a - b
mul = a * b
div = a / b

# 結果を画面に出す
print("足し算:", add)
print("引き算:", sub)
print("掛け算:", mul)
print("割り算:", div)
