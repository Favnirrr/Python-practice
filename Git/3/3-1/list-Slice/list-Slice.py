# スライス
# リストの一部を取り出す
# リスト[ 開始位置 : 終了位置 ]
# リスト[ 開始位置 : 終了位置 : ステップ数 ]

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1番目の要素番号から3番目-1の要素番号まで取り出す
print(b[1:3])

# 開始位置を省略すると先頭から取り出す
print(b[:3])
# 終了位置を省略すると末尾まで取り出す
print(b[7:])
# 開始位置と終了位置を省略すると先頭から末尾まで取り出す
print(b[:])

# ステップ数を指定すると、指定した数だけ飛ばしながら取り出す
print(b[::2])