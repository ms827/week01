import sys
import time
st = time.time()
sys.stdin = open("input.txt", "rt")

# n = int(input())
# num_list = []
# for _ in range(1, n+1):
#     r = int(input())
#     num_list.append(r)
# num_list.sort()

# for i in range(len(num_list)):
#     print(num_list[i])

N = int(input())

numbers = []

for _ in range(N) : 
    numbers.append(int(input()))

# Bubble Sort
for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
for n in numbers : 
    print(n)