from collections import defaultdict
import heapq

N = int(input())
all_class = []

for i in range(N):
  id, start, end = map(int, input().split(' '))
  all_class.append([end, start])

rooms = []
all_class.sort(key=lambda x: -x[1])
start = all_class.pop()

heapq.heappush(rooms, start)

ans = 1

while all_class:
  prev_end, prev_start = rooms[0]
  end, start = all_class.pop()
  if prev_end <= start:
    heapq.heappop(rooms)
  heapq.heappush(rooms, [end, start])
  ans = max(len(rooms), ans)
print(ans)
