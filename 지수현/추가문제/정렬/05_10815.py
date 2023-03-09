import sys

sys.stdin = open("test.txt","rt")

N = int(input())
my_cards = set(input().split())
M = int(input())
given_cards = input().split()

sol = {}

print(" ".join("1" if x in my_cards else "0" for x in given_cards))