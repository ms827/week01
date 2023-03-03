N = int(input())

for j in range(N):
    result =''
    S = list(input())
    for i in S[2:]:
        result += i*int(S[0])
    print(result)