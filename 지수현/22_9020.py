import sys

def sosu (data):
    for i in range(2,data):
        if data%i==0:
            return False
    return True
        

N=int(sys.stdin.readline())
temp = [False, False] + [True]*10001
for _ in range(N):
    data = int(sys.stdin.readline())
    mid = data //2

    for i in range(mid-1):
        if sosu(mid-i) and sosu(mid+i):
            print(mid-i,mid+i)
            break 
    