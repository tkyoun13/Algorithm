from collections import deque

N = int(input())
nums = list(map(int, input().split()))

dq = deque((i+1, num) for i, num in enumerate(nums))

result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(-move)

print(' '.join(map(str, result)))