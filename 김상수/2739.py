import sys
sys.stdin=open("input.txt", "rt")

a= int(input())

for i in  range(1,10):
    print(a,'*', i , '=', i * a)
    i += 1