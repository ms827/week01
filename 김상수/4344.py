import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
for _ in range(n):
    score = list(map(int, input().split()))
    a = score[0]
    score = score[1:]
    sum_score = sum(score)
    ave = sum_score / a

    count = 0
    for i in score:
        if i > ave: count += 1
        
    per = count/a*100
    
    print("{:.3f}%".format(per))