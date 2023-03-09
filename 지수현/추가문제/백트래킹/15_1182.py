import sys

N,S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = 0
def dfs(next,cnt,n,visited):
    global result
    if cnt == n:
        if sum(visited) == S:
            result +=1
        return 
    
    for i in range(next,N):
        visited.append(arr[i])
        dfs(i+1,cnt+1,n,visited)
        visited.pop()

for i in range(1,N+1):
    dfs(0,0,i,[])

print(result)

