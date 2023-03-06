import sys

def recursive(start,current,total,visited):
    global min_value

    if len(visited) == N:
        if cost[current][start] !=0:
            min_value = min(min_value, total + cost[current][start])
            return

    for next in range(N):
        if cost[current][next] !=0 and next not in visited and total < min_value:
            visited.append(next)
            recursive(start,next,total+cost[current][next],visited)
            visited.pop() 

N = int(sys.stdin.readline())
cost = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

min_value = sys.maxsize

for i in range(N):
    recursive(i,i,0,[i])
print(min_value)