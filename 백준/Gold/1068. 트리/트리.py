import sys

input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
delete = int(input())
cnt = 0

def dfs(node, parent):
    parent[node] = -2
    for i in range(len(parent)):
        if node == parent[i]:
            dfs(i, parent)


dfs(delete, parent)

for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        cnt += 1
print(cnt)