# 価格表のデータを辞書に格納する
prices = {'banana': 300, 'apple': 200, 'mango': 400}

# 辞書のデータを列挙する
print(prices.keys()) # dict_keys型が返される
print(list(prices.keys())) # list型に変換して表示する
# リンゴの価格を表示する
print(prices['apple']) #200

# データを整列して表示
print(sorted(prices.keys())) # ['apple', 'banana', 'mango']