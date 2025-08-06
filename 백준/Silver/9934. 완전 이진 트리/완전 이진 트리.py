import sys

K = int(input())
nodes = list(map(int, input().split()))
levels = [[] for _ in range(K)] #각 level별로 노드 저장

#재귀 사용
#left->root->right (inorder)
def build_tree(start, end, level):
    if start > end:
        return
    mid = (start + end) // 2 #tree의 root index
    levels[level].append(nodes[mid]) #현재 level에 root 저장
    build_tree(start, mid - 1, level + 1) #왼쪽 서브트리
    build_tree(mid + 1, end, level + 1) #오르쪽 서브트리

build_tree(0, len(nodes) - 1, 0)

for i in levels:
    print(' '.join(map(str, i)))