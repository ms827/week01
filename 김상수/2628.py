import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")

A, B = map(int, input().split())
n = int(input())
x_list = [0,B]
y_list = [0,A]
for _ in range(1, n+1):
    x, y = map(int, input().split())
    if x == 0: x_list.append(y)
    else: y_list.append(y)

x_list.sort()
y_list.sort()

a_list = [] 
b_list = []   
for i in range(1, len(x_list)):
    r = x_list[i]-x_list[i-1]
    a_list.append(r)
for e in range(1, len(y_list)):
    h = y_list[e]-y_list[e-1]
    b_list.append(h)
    
print(max(a_list) * max(b_list))