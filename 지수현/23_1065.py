import sys
N = int(sys.stdin.readline())
count = 0
a=True
for i in range(1,N+1):
    if i < 100:
        count+=1
    else:
        temp = [int(j) for j in str(i)]
        result = temp[0] - temp[1]
        for j in range(1,len(temp)-1):
            if temp[j] -temp[j+1] == result:
                a=True
            else:
                a = False
                break
        if a:
            count+=1
print(count)
                
                


