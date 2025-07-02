from collections import deque

n, k = map(int, input().split())

def bfs():
    visited = [-1] * 100001
    visited[n] = 0
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        
        for next in (cur * 2, cur - 1, cur + 1):  
            if 0 <= next <= 100000 and visited[next] == -1:
                if next == cur * 2:
                    visited[next] = visited[cur]      # 순간이동은 0초
                    queue.appendleft(next)           # 우선적으로 탐색
                else:
                    visited[next] = visited[cur] + 1  # 걷기는 1초
                    queue.append(next)

    return visited[k]

print(bfs())