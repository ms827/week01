import sys
sys.stdin=open("input.txt", "rt")

result_list = []
for i in range(1, 10):
    result_list.append(int(input()))
    i += 1
    
print(max(result_list))
print(result_list. index(max(result_list))+1)
