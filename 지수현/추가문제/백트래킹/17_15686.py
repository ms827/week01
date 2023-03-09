import sys
from itertools import combinations
sys.stdin = open('추가문제/백트래킹/test.txt','rt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = sys.maxsize
home = []
store = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i,j])
        elif arr[i][j] == 2:
            store.append([i,j])           


for chic in combinations(store,M):
    chicken_min = 0
    for ho in home:
        temp = sys.maxsize
        for j in range(M):
            temp = min(temp,abs(ho[0]-chic[j][0])+abs(ho[1]-chic[j][1]))
        chicken_min +=temp
    result = min(result,chicken_min)
print(result)
