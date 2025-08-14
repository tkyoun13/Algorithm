import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque([]) # 좌표를 넣으므로 []

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j, 0])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    last_day = 0
    while queue:
        y, x, day = queue.popleft()
        last_day = day
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 안 익은 토마토 일 때
            if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
                box[ny][nx] = 1 #토마토를 익게 함
                queue.append((ny, nx, day + 1))

    return last_day

result_day = bfs()

is_possible = True
for row in box:
    if 0 in row:
        is_possible = False
        break

if is_possible:
    print(result_day)
else:
    print(-1)