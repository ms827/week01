import sys
def recursive(N,start,end):
    if N==1:
        temps.append([start,end])
        return

    recursive(N-1,start, 6-end-start)
    temps.append([start,end])
    recursive(N-1,6-end-start,end)

def result(N):
    if N < 21:
        recursive(N,1,3)
        print(2**N - 1)
        for temp in temps:
            print(*temp)
    else:
        print(2**N - 1)


N = int(sys.stdin.readline())
temps = []
result(N)