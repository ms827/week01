import sys
sys.stdin=open("input.txt", "rt")

nan_list = []
for i in range(9):
    nan_list.append(int(input))
from itertools import combinations
real_list = list(combinations(nan_list, 7))

