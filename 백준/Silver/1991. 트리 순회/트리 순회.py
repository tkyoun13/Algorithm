import sys

input = sys.stdin.readline

tree = {}

n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == '.':
        return
    print(node, end='') #root
    preorder(tree[node][0]) #left
    preorder(tree[node][1]) #right

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) #left
    print(node, end='') #root
    inorder(tree[node][1]) #right

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) #left
    postorder(tree[node][1]) #right
    print(node, end='') #root

preorder('A')
print()
inorder('A')
print()
postorder('A')