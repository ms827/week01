A = int(input())
B = list(map(int,input()))
result = 0
temp=[]
for b in B:
    temp.insert(0,A*b)
result = temp[-1]*100+temp[-2]*10+temp[-3]
for t in temp:
    print(t)
print(result)
