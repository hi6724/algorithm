from collections import defaultdict, deque

ans = 0
N = int(input())
q = deque()
values = [0 for _ in range(N+1)]
times = [0 for _ in range(N+1)]
graph = defaultdict(list)
next_nodes = defaultdict(list)
visited = [0 for _ in range(N+1)]
cnt = 0

for i in range(1, N+1):
    arr = list(map(int, input().split(" ")))
    values[i] = arr[0]
    if arr[1] == 0:
        q.append(i)
        continue
    for j in arr[2:]:
        graph[i].append(j)
        next_nodes[j].append(i)

while cnt < N:
    temp = set()
    while q:
        cur = q.popleft()
        needs = graph[cur]
        max_value = 0
        can_go = True
        for need in needs:
            if visited[need] == 0:
                can_go = False
                break
            max_value = max(max_value, times[need])
        if not can_go:
            continue
        times[cur] = values[cur]+max_value
        visited[cur] = 1
        for node in next_nodes[cur]:
            if visited[node] == 0:
                temp.add(node)
    q.extend(list(temp))
    cnt += 1
print(max(times))
