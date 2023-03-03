C = int(input())
for i in range(C):
    count=0
    students= list(map(int,input().split()))
    score_sum = sum(students[1:])/students[0]
    for student in students[1:]:
        if student > score_sum:
            count+=1
    print(f'{(count/students[0])*100:.3f}%')
    