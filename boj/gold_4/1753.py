import heapq
import math
from collections import defaultdict

n, m = map(int, input().split(' '))
start = int(input())

visited = defaultdict(bool)
graph = defaultdict(list)
distance = [math.inf]*(n+1)
q = []

for i in range(m):
  a, b, c = map(int, input().split(' '))
  graph[a].append((b, c))

heapq.heappush(q, (0, start))
distance[start] = 0

while q:
  value, node = heapq.heappop(q)
  if visited[node]:
    continue

  visited[node] = True
  next_nodes = graph[node]

  for next_node, next_value in next_nodes:
    total_value = next_value + value
    if total_value < distance[next_node]:
      heapq.heappush(q, (total_value, next_node))
      distance[next_node] = total_value

for i in (range(1, n+1)):
  print(distance[i] if distance[i] != math.inf else "INF")
