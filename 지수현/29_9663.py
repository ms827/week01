import sys
N = int(sys.stdin.readline())

cnt = 0
def check(x,i,visited):
    for i in range(N):
        
def dfs(x,y,visited):
    global cnt

    if cnt == N:
        count+=1
        return
    
    for i in range(N):
        if visited[i] == False and check(x,i):
            visited[i] = True
            cnt+=1
            dfs(x,i,visited)
            cnt-=1
            visited[i] = False

for i in range(N):
    dfs(i,i,[i])