import sys
import heapq
input = sys.stdin.readline

N = int(input())

min_q = []
max_q = []
ans = []
for i in range(N):
  num = int(input())
  if len(min_q) == len(max_q):
    heapq.heappush(max_q, num)
    temp = heapq.heappop(max_q)
    heapq.heappush(min_q, -temp)
  else:
    heapq.heappush(min_q, -num)
    temp = heapq.heappop(min_q)
    heapq.heappush(max_q, -temp)

  ans.append(-min_q[0])

for i in ans:
  print(i)
