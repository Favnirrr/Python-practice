# 可変長引数
# 引数の数が不定の場合に使用する
# 引数の前に*をつけると可変長引数になる
# 適当な数の引数をタプルとして受け取る

# 入力された数値を全て足し合わせる関数
def sum(*args):
    # *args内要素の型に応じて初期値を設定する
    if isinstance(args[0], int):
        v = 0
    elif isinstance(args[0], str):
        v = ""
    else:
        raise TypeError("引数の型が不正です")
    
    for n in args:
        v += n
    return v

print(sum(1, 2, 3, 4, 5)) # 15
print(sum(1, 2, 3)) # 6
print(sum(1, 2)) # 3

print(sum("a", "b", "c"))   # abc