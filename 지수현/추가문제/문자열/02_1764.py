import sys
sys.stdin = open("test.txt","rt")

N,M = map(int,input().split())
dic = {}
temp1 = set()
temp2 = set()
for _ in range(N): 
    temp1.add(input())
for _ in range(M): 
    temp2.add(input())
result = sorted(temp1&temp2)
print(len(result),*result)