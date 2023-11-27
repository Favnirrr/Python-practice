count = 0
raw_data = []
ans_data = []

count = int(input())
for i in range(count):
    raw_data = input().split()
    print(raw_data)
    # 出発まで
    start = int(raw_data[0])
    # 移動
    move = int(raw_data[1])
    # 到着まで
    end = int(raw_data[2])
    end = 24 - end

    # 1回の移動時間
    ans_data.append(start + move + end)
    print(ans_data[i])
    
print(min(ans_data))
print(max(ans_data))