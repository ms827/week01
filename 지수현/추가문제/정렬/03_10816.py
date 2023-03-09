import sys

sys.stdin = open("test.txt","rt")

N = int(input())
my_cards = input().split()
M = int(input())
check_cards = input().split()
sol = {}
for check_card in check_cards:
    sol[check_card] = 0

for my_card in my_cards:
    if my_card in sol.keys():
        sol[my_card]+=1

for check_card in check_cards:
    print(sol[check_card], end=' ')