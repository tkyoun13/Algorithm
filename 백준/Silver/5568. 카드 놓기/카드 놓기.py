import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

results_set = set() 

for p in permutations(cards, k):
    number_str = "".join(p)
    results_set.add(number_str)

print(len(results_set))