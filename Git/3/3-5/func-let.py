# 関数は変数に代入できるのか？

# 関数を定義
def mul_func(a, b):
    return a * b

def div_func(a, b):
    return a / b

# 関数を変数に代入
func = mul_func
func2 = div_func

# 変数に代入した関数を実行
result = func(2, 3)
result2 = func2(10, 5)

print(result)
print(result2)

# 関数を引数に指定
def calc_5_3(func):
    return func(5, 3)

# 引数に関数を指定して実行
result3 = calc_5_3(mul_func)
print(result3)