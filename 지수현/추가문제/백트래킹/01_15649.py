import sys
n,m = map(int,sys.stdin.readline().split())
s = []
result = []
def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
        result.append(s)
        
dfs()