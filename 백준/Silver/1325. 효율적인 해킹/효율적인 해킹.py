from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
com = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    q = deque([x])
    cnt = 0

    visited = [0] * (n+1)
    visited[x] = 1

    while q:
        v = q.popleft()

        for w in graph[v]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)
                cnt += 1
        
    return cnt

for i in range(1, n+1):
    com.append(bfs(i))

for i in range(len(com)):
    if com[i] == max(com):
        print(i+1, end= ' ')