# 1-6までのランダムな整数を生成する

import random

# 最大繰り返し回数を定義
MAX = 100

# スコア
score = 0

# MAX回繰り返す
for i in range(1,MAX+1):
    dice = random.randint(1, 6)
    # スコアに加算
    # もしスコアが50を超えたら、diceをスコアから減算する
    if score > 50:
        print( i, "回目 スコア:",score ," ", dice, "点を足して合計は", score + dice)
        score -= dice
    else:
        print( i, "回目 スコア:",score ," ", dice, "点を引いて合計は", score - dice)
        score += dice