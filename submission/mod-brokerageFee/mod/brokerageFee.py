def brokerageFee(price):
    # 仲介手数料を計算
    # 200万円以下のとき 価格*5%
    # 200万円超300万円以下のとき 価格*4%+2万円
    # 300万円超のとき 価格*3%+6万円
    if price <= 200:
        brokerageFee = price * 0.05
    elif price <= 300:
        brokerageFee = price * 0.04 +2
    else :
        brokerageFee = price * 0.03 +6

    # 仲介手数料を表示
    print("仲介手数料は", brokerageFee, "万円です。")