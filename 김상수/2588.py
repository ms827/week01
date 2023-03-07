import sys
sys.stdin=open("input.txt", "rt")

A = int(input())
B = input()

a = A * int(B[2])
b = A * int(B[1])
c = A * int(B[0])
print(a)
print(b)
print(c)
print(a + 10*b +100*c)
