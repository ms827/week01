import sys
N = int(sys.stdin.readline())
arrs = [[] for _ in range(51)]
results = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    length = len(word)
    if word not in arrs[length]:
        arrs[length].append(word)

for i in range(len(arrs)):
    if arrs[i]:
        arrs[i].sort()
        results.extend(arrs[i])

print(*results)