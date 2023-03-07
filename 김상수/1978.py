import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
number_list = list(map(int, input().split()))
sosu = 0
for t in range(n):
    gong = 0
    k = number_list[t-1]
    for i in range(1, k+1):
        if k%i == 0:
            gong += 1
    if gong ==2:
        sosu += 1

print(sosu)