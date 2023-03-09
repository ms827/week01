import sys


def dfs(depth,idx):
    global min_value

    if depth == N//2:
        total1,total2=0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    total1 += arr[i][j]

                elif not visited[i] and not visited[j]:
                    total2 += arr[i][j]

        min_value = min(min_value,abs(total1-total2))
        return
    
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False


N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
visited = [False] * N
min_value = int(1e9)

dfs(0,0)
print(min_value)

