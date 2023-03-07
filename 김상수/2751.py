import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")


import sys
input = sys.stdin.readline
n = int(input())
num_list = []
for _ in range(1, n+1):
    r = int(input())
    num_list.append(r)
num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])