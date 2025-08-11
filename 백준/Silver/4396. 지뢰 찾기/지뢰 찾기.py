import sys
input = sys.stdin.readline

n = int(input().strip())
mine = [list(input().strip()) for _ in range(n)]
open = [list(input().strip()) for _ in range(n)]

dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

exploded = False

for i in range(n):
    for j in range(n):
        if open[i][j] == 'x' and mine[i][j] == '*':
            exploded = True
            break

ans = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if open[i][j] == 'x':
            if mine[i][j] == '*':
                pass
            else:
                cnt = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and mine[ni][nj] == '*':
                        cnt += 1
                ans[i][j] = str(cnt)

if exploded:
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                ans[i][j] = '*'

for i in range(n):
    print(''.join(ans[i]))