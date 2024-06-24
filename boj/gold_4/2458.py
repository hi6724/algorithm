n, m = map(int, input().split())
graph1 = [[] for _ in range(501)]
graph2 = [[] for _ in range(501)]
count = 0
for i in range(m):
    x, y = map(int, input().split())
    graph1[x].append(y)
    graph2[y].append(x)

for i in range(1, n + 1):
    ans = set()
    q = [i]
    visited = [i]
    while q:
        node = q.pop()
        for tt in graph1[node]:
            if tt not in visited:
                visited.append(tt)
                q.append(tt)
    for s in visited:
        ans.add(s)
    q = [i]
    visited = [i]
    while q:
        node = q.pop()
        for tt in graph2[node]:
            if tt not in visited:
                visited.append(tt)
                q.append(tt)
    for s in visited:
        ans.add(s)
    if len(ans) == n:
        count += 1
print(count)