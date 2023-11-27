count = 0
answer_count = 0
answer_idx = []

count = int(input())
for i in range(count):
    answer = input()
    ans_1st = answer[0]
    ans_2nd = answer[2]
    
    if ans_1st == "y" and ans_2nd == "y":
        continue
    
    answer_count += 1
    answer_idx.append(i + 1)

print(answer_count)
for i in range(len(answer_idx)):
    print(answer_idx[i])
    
