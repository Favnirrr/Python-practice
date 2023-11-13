# 関数の外側でvalueに100を代入
value = 100

def changeValue():
    # 関数の中でグローバル宣言
    global value
    value = 20

changeValue()
print(value)