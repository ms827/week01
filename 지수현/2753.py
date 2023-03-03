def f_result(A):
    if A % 4 == 0:
        if A % 400 == 0:
            return 1
        else:
            if A % 100 !=0:
                return 1
    return 0        

A = int(input())
print(f_result(A))