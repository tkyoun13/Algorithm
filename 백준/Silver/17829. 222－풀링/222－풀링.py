import sys
input = sys.stdin.readline

def pooling(matrix, x, y, size):
    if size == 2:
        nums = [
            matrix[x][y],
            matrix[x][y+1],
            matrix[x+1][y],
            matrix[x+1][y+1]
        ]
        nums.sort(reverse=True)
        return nums[1]
    
    half = size // 2
    values = [
        pooling(matrix, x, y, half),
        pooling(matrix, x, y + half, half),
        pooling(matrix, x + half, y, half),
        pooling(matrix, x + half, y + half, half)
    ]
    values.sort(reverse=True)
    return values[1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(pooling(matrix, 0, 0, N))