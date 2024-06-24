import math
import heapq
from collections import defaultdict

TC = int(input().strip())
ans = []
for tc in range(TC):
  graph = defaultdict(list)
  N, M, S = map(int, input().strip().split(' '))
  for i in range(M):
    end, start, time = map(int, input().strip().split(' '))
    graph[start].append((time, end))

  visited = defaultdict(bool)
  distance = defaultdict(lambda: math.inf)
  q = []
  heapq.heappush(q, (0, S))
  distance[S] = 0

  while q:
    time, node = heapq.heappop(q)
    next_nodes = graph[node]
    if visited[node]:
      continue
    visited[node] = True

    for next_time, next_node in next_nodes:
      total_time = next_time + time
      if distance[next_node] > total_time:
        heapq.heappush(q, (total_time, next_node))
        distance[next_node] = total_time
  temp = list(distance.values())

  ans.append(f'{len(temp)} {max(temp)}')
for a in ans:
  print(a)
