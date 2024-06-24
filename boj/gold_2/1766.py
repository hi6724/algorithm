from collections import defaultdict, deque
import heapq

graph = defaultdict(list)
indegree = defaultdict(int)

N, M = map(int, input().split(' '))
for i in range(1, M+1):
  first, second = map(int, input().split(' '))
  graph[first].append(second)
  indegree[second] += 1


result = []
q = []
for i in range(1, N+1):
  if indegree[i] == 0:
    heapq.heappush(q, i)

while q:
  cur = heapq.heappop(q)
  result.append(cur)
  for i in graph[cur]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(q, i)

for i in result:
  print(i, end=' ')
