from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush
import math

input = stdin.readline

n = int(input())
bus_num = int(input())
graph = defaultdict(list)
value_list = defaultdict(lambda: math.inf)

for _ in range(bus_num):
  start, end, value = map(int, input().split(' '))
  graph[start].append((value, end))

S, T = map(int, input().split(' '))
nearnest = [S] * (n + 1)


q = []
heappush(q, (0, S))

while q:
  cur_value, cur_node = heappop(q)
  if value_list[cur_node] < cur_value:
    continue

  for next_value, next_node in graph[cur_node]:
    total_value = next_value + cur_value
    if value_list[next_node] > total_value:
      value_list[next_node] = total_value
      nearnest[next_node] = cur_node
      heappush(q, (total_value, next_node))

path = []
tmp = T
while tmp != S:
  path.append(str(tmp))
  tmp = nearnest[tmp]

path.append(str(S))
path.reverse()

print(value_list[T])
print(len(path))
print(" ".join(path))
