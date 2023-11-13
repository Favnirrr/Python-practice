# 文字列の分割
# split()
# 文字列.split(区切り文字, 最大分割数)

s1 = "This is a pen."
s2 = "2023/11/13"
# 区切り文字を指定しないとき、空白文字で分割
print(s1.split())    # ['This', 'is', 'a', 'pen.']  空白文字がなくなる

# 区切り文字を指定するとき、指定した文字で分割
print(s1.split("s")) # ['Thi', ' i', ' a pen.'] sがなくなる
print(s2.split("/")) # ['2023', '11', '13'] /がなくなる

# 最大分割数を指定するとき、指定した数で分割
print(s2.split("/", 1)) # ['2023', '11/13'] 1回だけ分割

# 分割後に結合
# 文字列の分割後はリストになるので、join()を使って結合する
# 区切り文字.join(リスト)
print(" ".join(s1.split())) # This is a pen.

# 日付の書式変更
# s2の/を-に変更する
print("-".join(s2.split("/"))) # 2023-11-13

# 文字列の置換
# replace()
# 文字列.replace(置換前, 置換後 [, 置換数])
print(s1.replace("pen", "apple"))  # This is a apple.

print("------")

# 文字列の検索
# find()
# 文字列.find(検索文字列 [, 検索開始位置 [, 検索終了位置]])
# "This is a pen."
print(s1.find("is"))    # 2 "|This is a pen."
print(s1.find("is", 3)) # 5 "Thi|s is a pen."