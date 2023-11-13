# for構文でenumerate()を使う
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

# enumerate()の動作を確認する
print(list(enumerate(fruits)))