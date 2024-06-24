from collections import defaultdict


def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]


def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y


parent = defaultdict(int)

N = int(input())
M = int(input())
for i in range(N+1):
  parent[i] = i

q = []
for i in range(M):
  a, b, c = map(int, input().split(' '))
  q.append([c, a, b])
q.sort(reverse=True)


ans = 0
while q:
  value, a, b = q.pop()
  if find(parent, a) != find(parent, b):
    union(parent, a, b)
    ans += value
print(ans)
