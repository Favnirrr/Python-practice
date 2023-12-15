import copy

### 回答用返り値
ans = 0

### 度数と在庫
N = int(input())
# N個の要素を持つリストを作成
stock = [0] * N
for i in range(0, N):
    stock[i] = int(input())

### お客さんの注文
M = int(input())
desire_R = [0] * M
desire_L = [0] * M
for i in range(0, M):
    desire_R[i], desire_L[i] = map(int, input().split())

### 注文を処理 
# cnt = お客さんの数
for cnt in range(M):
    R = desire_R[0] -1
    L = desire_L[0] -1
    tmp = copy.copy(stock) # stockの状態をコピー

    # 右レンズを購入できるか
    if tmp[R] > 0 : 
        tmp[R] -= 1
        # 左レンズを購入できるか
        if tmp[L] > 0:  
            tmp[L] -= 1
            # 購入可能
            stock[R] = stock[R] -1
            stock[L] = stock[L] -1
            ans += 1
    
    del desire_R[0]
    del desire_L[0]

print(ans)