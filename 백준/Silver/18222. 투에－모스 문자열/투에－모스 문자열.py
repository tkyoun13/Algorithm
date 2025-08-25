import sys

k = int(sys.stdin.readline())

def find_char(n):
    if n == 1:
        return 0
    
    p = 1
    while p * 2 < n:
        p *= 2

    return 1 - find_char(n - p) #반전되기 이전 값

print(find_char(k))