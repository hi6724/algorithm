from collections import defaultdict, deque

N, M = map(int, input().split(' '))
graph = defaultdict(list)
indegree = defaultdict(int)

for i in range(M):
  data = list(map(int, input().split(' ')[1:]))
  for i in range(1, len(data)):
    graph[data[i-1]].append(data[i])
    indegree[data[i]] += 1

q = deque()
ans = []
for i in range(1, N+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  num = q.popleft()
  ans.append(num)
  for i in graph[num]:
    indegree[i] -= 1
    if indegree[i] == 0:
      q.append(i)

if len(ans) != N:
    print(0)
else:
    for i in ans:
        print(i)
