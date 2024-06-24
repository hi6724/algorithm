from collections import defaultdict
from heapq import heappop,heappush


N,M,R = map(int,input().split(' '))
items = list(map(int,input().split(' ')))

ans=-1
graph=defaultdict(list)
for i in range(R):
  a,b,c = map(int,input().split(' '))
  graph[a-1].append((c,b-1))
  graph[b-1].append((c,a-1))

for start in range(N):
  # start 에서 갈수 있는 곳 알아보기
  distance=defaultdict(lambda: 9999999999)
  visited=defaultdict(bool)
  distance[start]=0
  q=[]
  heappush(q,(0,start))
  while q:
    value,node = heappop(q)
    if visited[node]:
      continue
    visited[node]=True
    next_nodes = graph[node]
    
    for next_value,next_node in next_nodes:
      if distance[next_node] > value + next_value:
        distance[next_node] = value + next_value
        heappush(q,(value + next_value,next_node))
  temp_ans = 0
  for key in distance:
    if distance[key]<=M:
      temp_ans+=items[key]
  ans=max(ans,temp_ans)

print(ans)    