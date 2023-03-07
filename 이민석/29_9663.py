import sys
import time
st = time.time()  # 시작 시간 저장
sys.stdin=open("이민석\input.txt", "rt")

n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 같은 열에 있는지 검사
        if row[x] == row[i]:
            return False
        # 대각선 방향에 있는지 검사
        if abs(row[x] - row[i]) == x - i:
            return False
    return True
    

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)






















"""
def n_queens (i, col):
    n = len(col) - 1
    if (promising(col, i)):
        if (i == n):
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)

def promising (i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

n = 8
col = [0] * (n + 1)
n_queens(0, col)
"""
print("time :", time.time() - st)
