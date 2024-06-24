# https://www.acmicpc.net/problem/2468

import copy

n = int(input())

graph = []
max_value = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    if max(data) > max_value:
        max_value = max(data)
ans = 0
for v in range( max_value):
    count = 0
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            q = []
            if temp[i][j] > v:
                count += 1
                q = [(i, j)]
            while q:
                x, y = q.pop()
                temp[x][y] = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if temp[nx][ny] > v:
                            q.append((nx, ny))
    if count > ans:
        ans = count
print(ans)
