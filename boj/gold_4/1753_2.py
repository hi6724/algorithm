import heapq
import math
from collections import defaultdict

n, m = map(int, input().split(' '))
start = int(input())
visited = defaultdict(bool)
graph = defaultdict(list)
for i in range(m):
  a, b, c = map(int, input().split(' '))
  graph[a].append((b, c))

distance = [math.inf]*(n+1)
q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for next_node, value in graph[now]:
    cost = dist+value
    if cost < distance[next_node]:
      distance[next_node] = cost
      heapq.heappush(q, (cost, next_node))
for i in (range(1, n+1)):
  print(distance[i] if distance[i] != math.inf else "INF")
