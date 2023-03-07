import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")

n = int(input())
if n < 100:
    print(n)
    
elif n == 1000: print(144)

else:
    
    count = 99
    for i in range(100, n+1):
        a, b, c = map(int, str(i))
        if 2*b == a + c:
         count += 1
        
    print(count)
