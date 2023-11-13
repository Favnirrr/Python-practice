# 集合型
# 複数の値を記録でき、重複した値を持たない
# また、順序を持たないため、
# インデックスを指定して値を取得することはできない

# 集合型の定義
# {} で囲む
colors = {"red", "green", "blue"}
print(colors)

# 空の集合型の定義
# set() で定義する
e_set = set()

# 要素の追加
e_set.add("yellow")

# 差分
# 左辺にあって右辺にない要素を取得する
a = {"red", "green", "blue"}
b = {"red", "blue", "pink"}

print(a - b)

# 要素に含まれるかを調べる
# in を使う
colors = {"red", "green", "blue"}
print("green" in colors)