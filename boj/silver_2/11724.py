# https://www.acmicpc.net/problem/11724 3초
from collections import deque
import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
graph = [[] for _ in range(1001)]

for i in range(m):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = {}
count = 0
for i in range(n + 1):
    visited[i] = 0
for i in range(1, n+1):
    if visited[i] == 1:
        continue
    q = [i]
    while q:
        node = q.pop()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)

    count += 1
print(count)