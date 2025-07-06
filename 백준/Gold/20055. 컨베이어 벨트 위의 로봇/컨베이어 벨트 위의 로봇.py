from collections import deque

def simulate(N, K, A):
    durability = deque(A)  # 벨트 내구도
    robots = deque([False] * N)  # 로봇이 있는 위치 
    
    step = 0

    while True:
        step += 1

        # 1. 벨트 + 로봇 회전
        durability.rotate(1)
        robots.rotate(1)
        robots[-1] = False  # 내리는 위치에서 로봇 내림

        # 2. 로봇 이동
        for i in range(N - 2, -1, -1): 
            if robots[i] and not robots[i+1] and durability[i+1] > 0:
                robots[i] = False
                robots[i+1] = True
                durability[i+1] -= 1
        robots[-1] = False  # 내리는 위치에서 로봇 내림

        # 3. 로봇 올리기
        if durability[0] > 0:
            robots[0] = True
            durability[0] -= 1

        # 4. 종료 조건 확인
        zero_count = durability.count(0)
        if zero_count >= K:
            return step


N, K = map(int, input().split())
A = list(map(int, input().split()))


result = simulate(N, K, A)


print(result)
