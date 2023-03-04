import sys
def recursive(N):
    if N < 1:
        return 1
    else:
        return N*recursive(N-1)

N = int(sys.stdin.readline())
print(recursive(N))
