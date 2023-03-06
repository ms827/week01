import sys
def sol(x):
    for i in range(N):
        if temp[x] != temp[i] and abs(row[x] - row[i]) 

def dfs(x):
    global result

    if x==N:
        result+=1
        return
    
    else:
        for i in range(N):
            temp[x] = i
            if sol(x):
                dfs(x+1)   

N = int(sys.stdin.readline())
temp = []
result = 0
dfs(0)
print(result)