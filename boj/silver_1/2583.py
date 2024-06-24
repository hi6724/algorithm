from collections import deque

n, m, k = map(int, input().split())
arr = [['O' for __ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[k][j] = 'X'
ans = []
for i in range(n):
    for j in range(m):
        q = deque()
        count = 0
        if arr[i][j] == "O":
            arr[i][j] = 1
            q.append([i, j])
            count += 1
        while q:
            x, y = q.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == "O":
                        arr[nx][ny] = arr[x][y] + 1
                        q.append([nx, ny])
                        count += 1
        if count != 0:
            ans.append(count)
ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')
