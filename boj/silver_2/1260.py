# https://www.acmicpc.net/problem/1260
from collections import deque
import heapq

n, m, start = list(map(int, input().split()))
graph = [[] for _ in range(10001)]
for i in range(m):
    node1, node2 = list(map(int, input().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in graph:
    i.sort(reverse=True)

q = deque()
q.append(start)
visited = []
while q:
    node = q.pop()
    if node not in visited:
        print(node, end=' ')
    visited.append(node)
    for i in graph[node]:
        if i not in visited:
            q.append(i)
print()
for i in graph:
    i.sort()
q = deque()
q.append(start)
visited = []
while q:
    node = q.popleft()
    if node not in visited:
        print(node, end=' ')
    visited.append(node)
    for i in graph[node]:
        if i not in visited:
            q.append(i)