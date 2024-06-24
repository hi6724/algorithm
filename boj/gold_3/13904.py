from collections import defaultdict
from heapq import heappop, heappush

N = int(input())  # <= 1000

works = defaultdict(list)
q = []

for i in range(N):
  d, w = map(int, input().split(' '))
  works[d].append(-w)

for i in range(N, max(list(works.keys()))):
  for work in works[i+1]:
    heappush(q, work)

score = 0
for i in range(N, 0, -1):
  for work in works[i]:
    heappush(q, work)
  if len(q) == 0:
    continue
  score += heappop(q)
print(-score)
