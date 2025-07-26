import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k 

    for i in range(k):
        op, val = input().split()
        val = int(val)

        if op == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True
        else:
            if val == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
