# https://www.acmicpc.net/problem/1389
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = []
for i in range(1, n + 1):
    temp = [0 for _ in range(n + 1)]
    q = deque()
    q.append(i)
    while q:
        node = q.popleft()
        arr = graph[node]
        for item in arr:
            if temp[item] == 0:
                temp[item] = temp[node] + 1
                q.append(item)
    ans.append([i, sum(temp)])
ans.sort(key=lambda x: x[1])
print(ans[0][0])
