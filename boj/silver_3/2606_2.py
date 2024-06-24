n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    start_node, finish_node = map(int, input().split())
    graph[start_node].append(finish_node)
    graph[finish_node].append(start_node)
for i in graph:
    i.sort()
visited = []
need_visit = [1]
while need_visit:
    node = need_visit.pop()
    if node not in visited:
        visited.append(node)
        need_visit.extend(graph[node])
print(len(visited) - 1)
