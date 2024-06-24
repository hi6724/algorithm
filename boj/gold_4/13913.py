from collections import deque, defaultdict
from heapq import heappop,heappush

N, K = map(int,input().split(' '))
distance_list = defaultdict(lambda:99999999999)
prev_pos_list = defaultdict(lambda:-1)

q = []
heappush(q,[0,N])

while True:
  distance,cur_pos = heappop(q)
  if cur_pos > 200000:
    continue

  if distance_list[cur_pos+1] > distance+1:
    heappush(q,[distance+1,cur_pos+1])
    distance_list[cur_pos+1] = distance+1
    prev_pos_list[cur_pos+1] = cur_pos

  if distance_list[cur_pos-1] > distance+1:
    heappush(q,[distance+1,cur_pos-1])
    distance_list[cur_pos-1] = distance+1
    prev_pos_list[cur_pos-1] = cur_pos

  if distance_list[cur_pos*2] > distance+1:
    heappush(q,[distance+1,cur_pos*2])
    distance_list[cur_pos*2] = distance+1
    prev_pos_list[cur_pos*2] = cur_pos


  if distance_list[K] != 99999999999:
    break

result = [K]
q = [K]
while q:
  node = q.pop()
  if node != N:
    q.append(prev_pos_list[node])
    result.append(prev_pos_list[node])

result.reverse()
print(len(result)-1)
print(" ".join(list(map(str,result))))