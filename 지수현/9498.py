score = int(input())

if score//90 == 1:
    print('A')
elif score//80 == 1:
    print('B')
elif score//70 == 1:
    print('C')
elif score//60 == 1:
    print('D')
else:
    print('F')