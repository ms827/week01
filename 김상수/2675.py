import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)
    for x in b:
        print(x * a, end="")
    print()
    