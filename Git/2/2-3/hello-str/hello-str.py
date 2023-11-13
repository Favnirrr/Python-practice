print("Hello Python!")
print('Hello Python!')

print("Hello 'Python'!")
print('Hello "Python"!')

print('Hello \'Python\'!')
print("Hello \"Python\"!")

str = """
今日はいい天気です
明日もいい天気です
明後日は雨です
"""
print(str)

str = """\
今日はいい天気です
明日もいい天気です
明後日は雨です\ 
"""
# 末尾の\は、三重引用符の改行前に記述！！
# \""" は不可。
print(str)

