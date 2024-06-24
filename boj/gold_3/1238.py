import heapq
import math
from collections import defaultdict

N, M, X = map(int, input().split(' '))
graph = defaultdict(list)
for i in range(M):
  S, E, T = map(int, input().split(' '))
  graph[S].append((T, E))

to_party = defaultdict(int)
to_home = defaultdict(int)
for start in range(1, N+1):
  q = []
  visited = defaultdict(bool)
  distance = defaultdict(lambda: math.inf)
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    value, node = heapq.heappop(q)
    next_nodes = graph[node]
    if visited[node]:
      continue
    visited[node] = True

    for next_value, next_node in next_nodes:
      total_value = next_value + value
      if total_value < distance[next_node]:
        distance[next_node] = total_value
        heapq.heappush(q, (total_value, next_node))

  to_party[start] = distance[X]
  if start == X:
    for i in range(1, N+1):
      to_home[i] = distance[i]

ans = -1
for i in range(1, N+1):
  ans = max(ans, to_party[i]+to_home[i])

print(ans)
