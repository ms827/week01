import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")

n = int(input())
multi = 1
for i in range(1, n+1):
    multi = multi * i
    
print(multi)