# 入力した文字列の指定番目の文字を取り出す

# ターミナルから入力受付
inputStr = input("文字列を入力してください: ")
# ターミナルから入力受付
inputNum = int(input("何番目の文字を取り出しますか: "))
# 指定番目の文字を取り出す
outputStr = inputStr[inputNum - 1]

# 結果を表示
print(outputStr)