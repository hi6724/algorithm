import sys
from collections import deque
input = sys.stdin.readline

tc = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while(1):
    tc += 1
    n = int(input().rstrip())
    if n == 0:
        break

    cave = [[0 for _ in range(n)] for _ in range(n)]
    coin = [[9999999 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row = (input().rstrip()).replace(' ', '')
        for j, char in enumerate(row):
            if char != " ":
                cave[i][j] = int(char)

    q = deque()
    q.append((0, 0))
    coin[0][0] = cave[0][0]

    while q:
        x, y = q.popleft()
        visited[0][0] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 > nx or 0 > ny or ny >= n or nx >= n:
                continue
            if not visited[nx][ny]:
                if coin[nx][ny] > coin[x][y] + cave[nx][ny]:
                    coin[nx][ny] = coin[x][y] + cave[nx][ny]
                    q.append((nx, ny))
    print(f"Problem {tc}: {coin[-1][-1]}")
