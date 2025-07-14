from collections import deque
import sys

input = sys.stdin.readline 
n = int(input())
dq = deque()

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith('push_front'):
        _, x = cmd.split()
        dq.appendleft(int(x))
    elif cmd.startswith('push_back'):
        _, x = cmd.split()
        dq.append(int(x))
    elif cmd == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif cmd == 'pop_back':
        print(dq.pop() if dq else -1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(0 if dq else 1)
    elif cmd == 'front':
        print(dq[0] if dq else -1)
    elif cmd == 'back':
        print(dq[-1] if dq else -1)
