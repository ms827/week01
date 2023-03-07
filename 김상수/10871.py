import sys
sys.stdin=open("input.txt", "rt")

N, X = map(int, input().split())
num = list(map(int, input().split()))
for i in range(1, N+1):
               if num[i-1] < X: print (num[i-1])
              