import sys
import time
st = time.time()
sys.stdin=open("input.txt", "rt")

def goldbach(g):
    if g == 2:
        sosu = True
    for j in range(2,g):
        if g % j == 0:
            sosu = False
            break
        else:
            sosu = True
    return sosu
    
n = int(input())

for _ in range(1, n+1):
    r = int(input())
    
    # A = r//2
    # B = A 
    # for a in range(0,A):
    #     if goldbach(A-a) == 'true' and goldbach(B+a) == 'true': break

    
    # print (A-a,' ',B+a)
    mid = r//2
    for a in range(mid):
            if goldbach(mid-a) == True and goldbach(mid+a) == True: break

    
    print (mid-a,mid+a)
    
    
        
print("time :", time.time() - st)

print(goldbach(6))