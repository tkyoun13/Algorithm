import sys

def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    s, t = line.split()
    print("Yes" if is_subsequence(s, t) else "No")