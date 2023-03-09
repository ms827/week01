import sys
sys.stdin = open("test.txt","rt")
digit = list(map(int,input().split()))
print(*sorted(digit))
