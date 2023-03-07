import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())
info = [0] * n
located = [False] * n
diag1 = [False] * (2 * n -1)
diag2 = [False] * (2* n -1)
ans = 0

def set(i):
    global ans
    for j in range(n):
        if not located[j] and not diag1[i+j] and not diag2[i-j+ n -1]:
            info[i] = j
            print(info)
            if i == n - 1:
                ans += 1
            else:
                located[j] = diag1[i+j] = diag2[i-j+ n -1] = True
                print(located)
                print(diag1)
                print(diag2)
                set(i+1)
                located[j] = diag1[i+j] = diag2[i-j+ n -1] = False
    
set(0)
print(ans)
print("time :", time.time() - st)
