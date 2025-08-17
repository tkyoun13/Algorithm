import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
result = []

while i < N and j < M:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

if i < N:
    result.extend(A[i:])
if j < M:
    result.extend(B[j:])

print(' '.join(map(str, result)))