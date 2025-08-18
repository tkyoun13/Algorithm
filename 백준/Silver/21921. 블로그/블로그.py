import sys

input = sys.stdin.readline

N, X = map(int,input().split())
visitors = list(map(int, input().split()))

window_sum = sum(visitors[:X])
max_visitors = window_sum
max_count = 1

for i in range(X, N):
    window_sum += visitors[i] - visitors[i - X] #window를 오른쪽으로 한 칸 이동

    if window_sum > max_visitors: #새로운 최댓값 갱신
        max_visitors = window_sum
        max_count = 1
    elif window_sum == max_visitors: #기존 최대값과 같은 값이 나온 경우
        max_count += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_count)