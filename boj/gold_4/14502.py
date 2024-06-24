# https://www.acmicpc.net/problem/14502
import copy
from collections import Counter
from collections import deque
from itertools import product, combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
ans = 0
n, m = map(int, input().split())
temp = (list(product([i for i in range(n)], [i for i in range(m)])))
wall_list = list(combinations(temp, 3))

for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
for walls in wall_list:
    temp = copy.deepcopy(arr)
    j = True
    for wall in walls:
        x, y = wall
        if temp[x][y] == 0:
            temp[x][y] = 1
        else:
            j = False
    if j == False:
        continue
    q = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    count = 0
    for i in range(n):
        count += (temp[i].count(0))
    if count > ans:
        ans = count
print(ans)