import sys
from sys import stdin
from collections import deque

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue.popleft()) #가장 왼쪽 요소 반환 및 삭제

def size():
    print(len(queue))

def empty():
    if (len(queue) == 0):
        print(1)
    else:
        print(0)

def front():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[0])

def back():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[-1])

N = int(stdin.readline())

for i in range(N):
    cmd = stdin.readline().split()

    if (cmd[0] == 'push'):
        push(int(cmd[1]))
    elif (cmd[0] == 'pop'):
        pop()
    elif(cmd[0] == 'size'):
        size()
    elif(cmd[0] == 'empty'):
        empty()
    elif(cmd[0] == 'front'):
        front()
    elif(cmd[0] == 'back'):
        back()