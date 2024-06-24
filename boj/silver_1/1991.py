from collections import deque
N = int(input())
tree = {}
 
for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
# 전위 순회
q = deque()
q.append('A')
ans = []
while q:
  node = q.popleft()
  if node == '.':
    continue
  ans.append(node)
  q.appendleft(tree[node][1])
  q.appendleft(tree[node][0])
for i in ans:
  print(i, end='')
print()
inorder('A')
print()
q = deque()
q.append('A')
ans = []
while q:
  node = q.popleft()
  if node == '.':
    continue
  ans.append(node)
  q.extendleft(tree[node])
for i in range(len(ans)):
  print(ans[-1-i], end='')