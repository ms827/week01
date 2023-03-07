import sys
sys.stdin=open("input.txt", "rt")

a,b,c,d = map(int, input().split())

x = d - b
y = c - a

min = a

if a >= b :
    min = b
if min >= x :
    min = x
if min >= y :
    min = y

print(min)