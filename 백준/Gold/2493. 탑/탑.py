import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

stack = []
answer = [0] * n

for i in range(n):
    current_height = heights[i]

    while stack and stack[-1][1] < current_height: #이전 탑들 중 현재 탑의 높이보다 작거나 같은 탑은 stack에서 제거
        stack.pop()

    if stack: #남아 있는 탑 들 중 가장 오른쪽에 있는 탑이 신호 수신
        answer[i] = stack[-1][0] + 1

    stack.append((i, current_height)) #현재 탑을 stack에 추가

#[0, 0, 2, 2, 4] -> '0 0 2 2 4'
print(' '.join(map(str, answer)))