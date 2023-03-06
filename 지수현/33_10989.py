import sys

N = int(sys.stdin.readline())
arr = [0]*10001
result=''
for _ in range(N):
    arr[int(sys.stdin.readline())]+=1

for j in range(10001):
    if arr[j] !=0:
        for i in range(arr[j]):
            print(j)