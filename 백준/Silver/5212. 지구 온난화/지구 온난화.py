import sys

input = sys.stdin.readline

R, C = map(int, input().split())
original_map = [list(input().strip()) for _ in range(R)]

new_map = [row[:] for row in original_map]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 50년 후 지도
for r in range(R):
    for c in range(C):
        if original_map[r][c] == 'X':
            sea_neighbors = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if not (0 <= nr < R and 0 <= nc < C): #지도 밖일 때
                    sea_neighbors += 1
                    continue

                if original_map[nr][nc] == '.':
                    sea_neighbors += 1

            if sea_neighbors >= 3:
                new_map[r][c] = '.'

# 새로운 지도
min_r, min_c = R, C
max_r, max_c = -1, -1

for r in range(R):
    for c in range(C):
        if new_map[r][c] == 'X':
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

for r in range(min_r, max_r + 1):
    print("".join(new_map[r][min_c : max_c + 1]))