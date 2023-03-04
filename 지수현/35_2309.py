import sys
def solution(total):
    length = len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if total - (arr[i]+arr[j]) == 100:
                return arr[i], arr[j]
            
arr = [int(sys.stdin.readline().strip()) for _ in range(9)]
total = sum(arr)
i,j = solution(total)
arr.remove(i)
arr.remove(j)
arr.sort()
for _ in arr:
    print(_)