import sys
sys.stdin=open("input.txt", "rt")

from itertools import combinations

nan_list = []
for _ in range(9):
    nan_list.append(int(input()))
    
real_list = list(combinations(nan_list, 7))
for i in range(36):
    if sum(real_list[i]) == 100 :
        seven_list = list(real_list[i])
        seven_list.sort()
        for m in range(7):
            print(seven_list[m])
        break   

