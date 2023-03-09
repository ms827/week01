import sys
m = int(sys.stdin.readline())
arr = [1, 5, 10, 50]
s = []
result = set()

def dfs(start):
    global result

    if len(s) == m:
        result.add(sum(s))
        return
    
    for i in range(start,len(arr)):
        s.append(arr[i])
        dfs(i)
        s.pop()

dfs(0)
print(len(result))