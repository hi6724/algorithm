import math
import sys
from collections import defaultdict


def find(parent, x):
  if parent[x] == x:
    return x
  else:
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


start = [-1, math.inf]
parent = defaultdict(int)
positions = []
queue = []

N = int(input())
for i in range(N+1):
  parent[i] = i

for i in range(N):
  x, y = map(float, input().split(' '))
  positions.append([x, y])

for i in range(N):
  for j in range(N):
    if i == j:
      continue
    x1, y1 = positions[i]
    x2, y2 = positions[j]
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    queue.append([distance, i, j])
queue.sort(reverse=True)


ans = 0
max_distance = -1
while queue:
  distance, start, end = queue.pop()
  if find(parent, start) == find(parent, end):
    continue
  ans += distance
  union(parent, start, end)
print(ans)
