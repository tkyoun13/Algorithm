from collections import deque

n, k = map(int, input().split())

people = deque(range(1, n + 1))
result = []


while people:
    # k-1만큼 회전시킨 뒤, 맨 앞에 오는 요소 제거
    people.rotate(-(k - 1))
    result.append(people.popleft())

print("<" + ", ".join(map(str, result)) + ">")
