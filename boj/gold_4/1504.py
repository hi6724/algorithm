import heapq
from collections import defaultdict
import math

n, m = map(int, input().split(' '))
visited = defaultdict(bool)
graph = defaultdict(list)
for i in range(m):
  a, b, c = map(int, input().split(' '))
  graph[a].append((b, c))
  graph[b].append((a, c))
s1, s2 = map(int, input().split(' '))


def dijkstra(start, end):
  if start == end:
    return 0
  distance = [math.inf]*(n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[1] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, value in graph[now]:
      cost = dist+value
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  return distance[end]


dist1 = dijkstra(1, s1)
dist2 = dijkstra(s1, s2)
dist3 = dijkstra(s2, n)

dist4 = dijkstra(1, s2)
dist5 = dijkstra(s2, s1)
dist6 = dijkstra(s1, n)

total1 = dist1+dist2+dist3
total2 = dist4+dist5+dist6
ans = min(total1, total2)
if ans == math.inf:
  print(-1)
else:
  print(ans)
'''
5 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

'''
