import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
for i in range(1, n+1):
    a ,b = map(int, input().split())
    print(a+b)
    i += 1
 