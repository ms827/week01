import sys
sys.stdin = open("추가문제/백트래킹/test.txt","rt")
N=1

def dfs(next,cnt,visited):
    if cnt == 6:
        print(*visited)
        return
    for i in range(next,len(arr)):
        visited.append(arr[i])
        dfs(i+1,cnt+1,visited)
        visited.pop()


while True:
    temp = list(map(int,input().split()))
    N = temp[0]
    arr = temp[1:]
    if N==0:
        break

    dfs(0,0,[])
    print()

    
    