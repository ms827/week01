import sys
w, h = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
temp = [[0,h],[0,w]]
result = 0

for _ in range(N):
    n, idx = map(int,sys.stdin.readline().split())

    #세로 경우의 수
    if n == 0:
        temp[0].append(idx)
        temp[0].sort()

    # 가로 경우의 수
    else:
        temp[1].append(idx)
        temp[1].sort()


for i in range(1,len(temp[1])):
    w = temp[1][i] - temp[1][i-1] 
    for j in range(1,len(temp[0])):
        h = temp[0][j] - temp[0][j-1]
        if w*h > result:
            result = w*h
print(result)
    