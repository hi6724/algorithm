from collections import defaultdict
from heapq import heappop, heappush
from itertools import permutations

N, M = map(int, input().split(' '))
board = []
visited = defaultdict(bool)
visited[M] = True

# 1<N<10
# 1->2, 1->3 ... 다익스트라로 최단경로 만들기
#

for i in range(N):
  row = list(map(int, input().split(' ')))
  board.append(row)
distances = []
for start in range(N):
  distance = defaultdict(lambda: 9999999999)
  distance[start] = 0
  q = []
  heappush(q, [0, start])
  while q:
    value, key = heappop(q)
    for i in range(N):
      if i == key:
        continue
      next_distance = board[key][i]
      if value+next_distance < distance[i]:
        distance[i] = value+next_distance
        heappush(q, [value+next_distance, i])

  distances.append(distance)


arr = [i for i in range(N)]
arr.pop(M)

ans = 99999999999999999
for perm in permutations(arr, N-1):
  start = M
  total_distance = 0
  for end in perm:
    total_distance += distances[start][end]
    start = end
  ans = min(ans, total_distance)
print(ans)
