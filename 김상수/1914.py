
import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")

x = int(input())
def hanoi(x):
    if x == 1: return 1
    elif x > 1 : return 2 * hanoi(x-1) + 1

def hanoi_top(start, middle, end, x):
    if x >=1:
     hanoi_top(start, end, middle, x-1)
     print(start, end)
     hanoi_top(middle, start, end, x-1)
    
if x <=20: print(hanoi_top(1,2,3,x))
    

    