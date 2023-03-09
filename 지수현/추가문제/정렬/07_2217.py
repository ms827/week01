import sys

sys.stdin = open("test.txt","rt")

N = int(input())
ropes = [int(input()) for i in range(N)]
ropes.sort()
max_weight = 0
for i in range(N):
    if ropes[i]*(N-i) > max_weight:
        max_weight = ropes[i]*(N-i)
print(max_weight)