# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

m, n, h = map(int, input().split())  # mn크기, h상자수
graph = []
q = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i, j, k])
    graph.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while (q):
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][
                nz] == 0:
            q.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day - 1)
