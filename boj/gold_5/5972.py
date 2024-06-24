import sys
from heapq import heappop, heappush
from collections import defaultdict, deque

INF = sys.maxsize
N, M = map(int, input().split(' '))

graph = defaultdict(list)
for i in range(M):
  a, b, c = map(int, input().split(' '))
  graph[a].append((b, c))
  graph[b].append((a, c))

visited = defaultdict(bool)
distance = defaultdict(lambda: INF)
distance[1] = 0
q = []
heappush(q, [0, 1])

while q:
  value, node = heappop(q)
  if visited[node]:
    continue
  visited[node] = True
  next_nodes = graph[node]
  for next_node, next_value in next_nodes:
    total_value = value + next_value
    if distance[next_node] > total_value:
      distance[next_node] = total_value
      heappush(q, [total_value, next_node])
print(distance[N])
