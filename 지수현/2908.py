N = list(input().split())
N[0] = ''.join(reversed(N[0])) 
N[1] = ''.join(reversed(N[1])) 
if N[0] > N[1]:
    print(N[0])
else:
    print(N[1])