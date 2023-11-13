# 文字列の生成
s1 = "Hello"
s2 = " World"
print(s1 + s2)
# 複数行に渡る文字列
s3 = """Hello
World"""
print(s3)
# 数値から文字列
s4 = str(100)
print(s4)

# 文字列に対する演算
# 結合
s5 = "!"
print(s5 * 3)   # !!!
# 文字列の長さ
s6 = "0123456789"
print(len(s6))  # 10
# 文字列の一部を取得
print(s6[4])    # 4

# 文字列のスライス
print(s6[1:4])  # 123
print(s6[:4])   # 0123
print(s6[3:3])  # 空文字
print(s6[0:9:2])    # 02468
print(s6[::3])  # 0369