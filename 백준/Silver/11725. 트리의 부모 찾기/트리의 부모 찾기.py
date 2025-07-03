import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n+1)

#간선 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        current = queue.popleft() #현재 노드 꺼냄
        for neighbor in graph[current]: #현재 노드의 인접 노드 탐색
            if not visited[neighbor]: #아직 방문하지 않은 노드일 때
                parent[neighbor] = current #부모 노드 설정
                visited[neighbor] = True 
                queue.append(neighbor) #큐에 추가

bfs(1)

#부모 노드 출력 (2번~n번)
for i in range(2, n + 1):
    print(parent[i])