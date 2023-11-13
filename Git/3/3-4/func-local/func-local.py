# 関数の外側でvalueに100を代入
value = 100

def changeValue():
    # 関数の中でvalueを変更
    value = 20

changeValue()
print(value)

# changeValue内のvalueと、関数の外側で定義したvalueは別物
# このように関数内で定義された変数は、関数内でしか使用できない
# このような変数をローカル変数と呼ぶ