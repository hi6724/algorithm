from collections import defaultdict, deque


N = int(input())

graph = defaultdict(list)

for i in range(N):
    arr = list(map(int, input().split(' ')))
    for j in range(len(arr)):
        if arr[j] == 1:
            graph[i].append(j)

for i in range(N):
    q = deque()
    q.extend(graph[i])
    ans = []
    while q:
        node = q.popleft()
        ans.append(node)
        next_nodes = graph[node]
        for node in next_nodes:
            if node not in ans:
                q.append(node)
    for j in range(N):
        if j in ans:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()