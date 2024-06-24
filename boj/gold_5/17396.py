import sys
from heapq import heappop, heappush
from collections import defaultdict, deque

INF = sys.maxsize


N, M = map(int, input().split(' '))
wards = list(map(int, input().split(' ')))
wards[-1] = 0

graph = defaultdict(list)
for i in range(M):
  a, b, c = map(int, input().split(' '))
  graph[a].append((b, c))
  graph[b].append((a, c))

visited = defaultdict(bool)
distance = defaultdict(lambda: INF)
distance[0] = 0

q = []
heappush(q, [0, 0])
while q:
  value, node = heappop(q)
  if visited[node]:
    continue
  visited[node] = True
  next_nodes = graph[node]
  for next_node, next_value in next_nodes:
    total_value = next_value+distance[node]
    if distance[next_node] > total_value and wards[next_node] == 0:
      distance[next_node] = total_value
      heappush(q, [total_value, next_node])


if distance[N-1] == INF:
  print(-1)
else:
  print(distance[N-1])
