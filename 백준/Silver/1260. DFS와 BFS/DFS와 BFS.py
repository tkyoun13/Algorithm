from collections import deque

#정점만 찾아나가는 방식식
def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')
    for W in graph[V]:
        if not visited_dfs[W]:
            dfs(W)

def bfs(V):
    queue = deque([V]) #pop메서드의 시간복잡도가 낮은 덱 내장 메서드 이용용
    visited_bfs[V] = True
    while queue:
        V = queue.popleft() #queue에 있는 첫번째 값 꺼냄
        print(V, end=' ')
        for W in graph[V]:
            if not visited_bfs[W]:
                visited_bfs[W] = True
                queue.append(W)

N, M, V = map(int, input().split())
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: #오름차순 정렬(낮은 숫자부터 탐색색)
    i.sort()

# dfs
dfs(V)
print()

# bfs
bfs(V)