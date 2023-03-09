import sys
N = sys.stdin.readline().rstrip()
s= []
result = []
def dfs():
    temp = ''
    if len(s) == len(N):
        for i in s:
            temp+=N[i]
        if int(temp) > int(N):
            result.append(temp)
        return
    
    for i in range(len(N)):
        if i not in s: 
            s.append(i)
            dfs()
            s.pop()

dfs()
result.sort()
if len(result) == 0:
    print(0)
else:
    print(result[0])

