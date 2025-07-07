from collections import deque
import sys
input = sys.stdin.readline

# 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, grid, n, m):
    dist = [[-1] * m for _ in range(n)]
    dist[start_x][start_y] = 0
    q = deque()
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 목표지점 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x, start_y = i, j


dist = bfs(start_x, start_y, grid, n, m)

# 출력
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
