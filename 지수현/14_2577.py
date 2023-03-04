num_dic = {}
for i in range(10):
    num_dic[i] = 0

N = list(int(input()) for i in range(3))
results = str(N[0]*N[1]*N[2])
for j in results:
    num_dic[int(j)] +=1

for i in num_dic.values():
    print(i)