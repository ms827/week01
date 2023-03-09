import sys
sys.stdin = open("D:/jungle/week/week01/week01/지수현/test.txt","rt")

arr = input().split('-')
result  = []
for i in arr:
    total = 0
    temp = i.split('+')
    for j in temp:
        total += int(j)
    result.append(total)


solution = result[0]
for i in range(1,len(result)):
    solution -= result[i]

print(solution)