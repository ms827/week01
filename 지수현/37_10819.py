import sys
def permutation(arr,r):
    result = []
    if r == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i]+arr[i+1:],r-1):
            result.append([elem]+rest)
    return result
    
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
m=0
for temp in permutation(arr,N):
    result = 0
    for j in range(1,len(temp)):
        result+=abs(temp[j-1] - temp[j])
    if result > m:
        m = result
print(m) 
