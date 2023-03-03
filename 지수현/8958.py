N = int(input())

for i in range(N):
    data = input()

    result = 0
    c=0

    for j in range(1,len(data)+1):
        if data[j-1] == 'O':
            result +=(c+1)
            c+=1
        else:
            c=0
    print(result)

