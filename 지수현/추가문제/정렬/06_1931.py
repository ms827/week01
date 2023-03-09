import sys
from itertools import permutations

sys.stdin = open("test.txt","rt")

N = int(sys.stdin.readline())

arr = sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x:(x[1],x[0]))

ans=end=0

for s,e in arr:
    if s >= end:
        ans+=1
        end = e

print(ans)