import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

counts = [0] * 100001 #각 숫자의 개수 저장

start = 0
max_len = 0

for end in range(N):
    counts[arr[end]] += 1 #윈도우 확장

    while counts[arr[end]] > K: #윈도우 축소
        counts[arr[start]] -= 1
        start += 1

    max_len = max(max_len, end - start + 1)

print(max_len)