from collections import defaultdict


N, target = map(int, input().split(' '))

graph = defaultdict(dict)
distance = [99999 for i in range(target+1)]
distance[0] = 0
for i in range(N):
    start, end, d = map(int, input().split(' '))
    if end-start > d and target >= end:
        try:
            if graph[end][start] > d:
                graph[end][start] = d
        except:
            graph[end][start] = d

for i in range(1, target+1):
    if graph[i]:
        for start, v in list(graph[i].items()):
            distance[i] = min(distance[start]+v, distance[i-1]+1, distance[i])
    else:
        distance[i] = distance[i-1]+1
print(distance[-1])