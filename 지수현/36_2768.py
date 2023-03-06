# https://kjhoon0330.tistory.com/15
import sys
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

N,M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

results = set(sum(i) for i in combination(arr,3))
o_s=0
for s in results:
    if s<=M and s>o_s:
        o_s=s
print(o_s)
