import sys

sys.stdin = open("test.txt","rt")

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A - 오름차순 B - 내림차순 or A - 내림차순 B -오름차순
A.sort(reverse=True)
B.sort()

total = 0

for i in range(len(A)):
    total += A[i]*B[i]

print(total)