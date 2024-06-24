from collections import defaultdict


def find(parent, x):
  if x == parent[x]:
    return x
  else:
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x


gates = int(input())
P = int(input())
airport = defaultdict(bool)
timeline = []
ans = 0
parent = [0]
for i in range(P):
  timeline.append(int(input()))
for i in range(1, gates+1):
  parent.append(i)


for limit in timeline:
  docking = find(parent, limit)
  if docking != 0:
    union(parent, docking, docking-1)
    ans += 1
  else:
    break
print(ans)
