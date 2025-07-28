import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())
    nums = []

    while len(nums) < M:
        nums += list(map(int, input().split()))

    max_heap = [] #왼쪽 -> (작은 수, 최대 힙)
    min_heap = [] #오른쪽 절반 -> (큰 수, 최소 힙)

    result = []

    for i in range(M):
        num = nums[i]

        # max_heap, min_heap 구성
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num) #max_heap: heapq는 최소힙이므로 음수로 push
        else:
            heapq.heappush(min_heap, num) #min_heap

        # min_heap, max_heap 크기 균형 맞추기
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if i % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    for i in range(0, len(result), 10):
        print(' '.join(map(str, result[i:i+10])))