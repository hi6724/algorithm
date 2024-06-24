from collections import deque


def bfs(graph, start_node):
    visited, need_visited = [], []
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            temp = sorted(graph[node], reverse=False)
            need_visited.extend(temp)
    return visited


def dfs(graph, start_node):
    visited, need_visited = [], []
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            temp = sorted(graph[node], reverse=True)
            need_visited.extend(temp)
    return visited


n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

temp = {}
for i in range(1, len(adj)):
    temp[i] = adj[i]

for i in (dfs(temp, v)):
    print(i, end=" ")
print()
for i in (bfs(temp, v)):
    print(i, end=" ")