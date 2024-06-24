from collections import defaultdict, deque

N, M, K, X = map(int, input().split(' '))

graph = defaultdict(list)
distance = [-1 for _ in range(N+1)]
distance[X] = 0

for i in range(M):
    start, end = map(int, input().split(' '))
    graph[start].append(end)

q = deque([X])
while q:
    cur = q.popleft()
    for node in graph[cur]:
        if distance[node] == -1:
            distance[node] = distance[cur]+1
            q.append(node)
exist = False

if K in distance:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
            check = True
else:
    print(-1)