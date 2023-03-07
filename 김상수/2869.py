import sys
sys.stdin=open("input.txt", "rt")
import math
a, b, c = map(int, input().split())

x = (c-b)/(a-b)
print(math.ceil(x))

"""
sum = 0
i = 1
while sum < c:
    sum += a
    if sum >= c: 
    
        break
    sum -= b
    i += 1
    
print(i)
"""