import sys

input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * N
found = False

def dfs(u, depth):
    global found

    if found:
        return
    if depth == 4:
        found = True
        return
    
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v, depth + 1)
    visited[u] = False #백트래킹 (방문 상태 되돌림)

for i in range(N): # 모든 노드 dfs 수행
    dfs(i, 0)
    if found:
        break

if found:
    print(1)
else:
    print(0)