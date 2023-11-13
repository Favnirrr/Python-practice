# 関数
# 関数の定義
# def 関数名(引数):
#     処理
#     return 戻り値

# 関数の呼び出し
# 関数名(引数)

# docstring
# 関数の説明を記述する
# 関数の先頭に記述する
# """で囲む

# 関数の定義
def mul(a, b):
    '''掛け算を行う関数'''
    return a * b

# 関数を使う
print(mul(2, 3))
print(mul(10, 3))

help(mul) # docstringを表示
# help(print)