import sys

sys.stdin = open("test.txt","rt")

N = int(input())
arrs = list(map(int,input().split()))
result = 0

for arr in arrs:
    cnt = 0
    
    if arr == 1:
        continue

    for i in range(2,arr+1):
        if arr%i==0:
            cnt+=1
    
    if cnt < 2:
        result+=1

print(result)