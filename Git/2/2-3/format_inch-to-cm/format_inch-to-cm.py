# format()メソッド
# インチをセンチメートルに変換
per_inch = 2.54
inch = 24
cm = inch * per_inch
# 文字列で説明を加える
desc = "{0}インチ = {1}センチメートル".format(inch, cm)
print(desc)