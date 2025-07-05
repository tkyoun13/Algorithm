N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
status = [['S'] * M for _ in range(N)]  # 초기 도미노 상태는 모두 'S'

direction = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

total_score = 0

for _ in range(R):
    # 공격수 입력
    ax, ay, d = input().split()
    ax, ay = int(ax) - 1, int(ay) - 1

    if status[ax][ay] == 'S':
        queue = [(ax, ay)]
        dx, dy = direction[d]

        while queue:
            x, y = queue.pop(0)
            if status[x][y] == 'F':
                continue

            h = board[x][y]
            total_score += 1
            status[x][y] = 'F'

            for step in range(1, h):
                nx, ny = x + dx * step, y + dy * step
                if 0 <= nx < N and 0 <= ny < M and status[nx][ny] == 'S':
                    queue.append((nx, ny))

    # 수비수 입력
    dx, dy = map(int, input().split())
    dx -= 1
    dy -= 1
    if status[dx][dy] == 'F':
        status[dx][dy] = 'S'

# 출력
print(total_score)
for row in status:
    print(' '.join(row))
