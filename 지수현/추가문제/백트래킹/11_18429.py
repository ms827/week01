import sys

weight = 500
N,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

s=[]
result=500
count = 0
def dfs(result):
    global count
    if result < 500:
        return
    
    if len(s) == N:
        count+=1
        return
        
    for i in range(len(arr)):
        if i not in s:
            s.append(i)
            result = result - K + arr[i]
            dfs(result)
            result = result + K - arr[i]
            s.pop()

dfs(result)
print(count)