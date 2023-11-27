# 30以下の奇数を返すイテレータ
def genOdd():
    i = 1
    while i <= 30:
        yield i # 一旦ここでストップし、値を返す
        i += 2  # もう一度この関数が呼び出されたとき、ここから再開

# イテレータオブジェクトを得る
it = genOdd()
for v in it:
    print(v)