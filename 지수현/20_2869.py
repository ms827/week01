import sys
import math
A,B,V = map(int,sys.stdin.readline().split())
temp1 = A-B
temp2= V-A
print(math.ceil(temp2/temp1)+1)