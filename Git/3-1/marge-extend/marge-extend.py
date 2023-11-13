# 2つのリストの作成
n1 = [1, 3, 5]
n2 = [2, 4, 6]
# 2つのリストを結合してn3に代入
n3 = n1 + n2

# n3を表示
print(n3)

# n1とn2を交互に結合
n4 = []
for i in range(len(n1)):
    n4.append(n1[i])
    n4.append(n2[i])
    
# n4を表示
print(n4)

a = [1, 2, 3]
a += [4, 5, 6]
print(a)

b = [11, 22]
b.extend([33, 44])
print(b)