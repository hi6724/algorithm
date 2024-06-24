import math
import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline


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
queue = []

N, M = map(int, input().split(' '))
for i in range(N+1):
  parent[i] = i

for i in range(M):
  a, b, c = map(int, input().split(' '))
  queue.append([c, a, b])
queue.sort(reverse=True)

ans = 0
max_distance = -1
while queue:
  distance, start, end = queue.pop()
  if find(parent, start) == find(parent, end):
    continue
  ans += distance
  max_distance = max(max_distance, distance)
  union(parent, start, end)
print(ans-max_distance)
