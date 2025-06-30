#dfs
def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결 쌍 수

graph = [[] for _ in range(n+1)] 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

dfs(graph, 1, visited)

print(visited.count(True) - 1)