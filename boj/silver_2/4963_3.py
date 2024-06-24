while True:
    n, m = list(map(int, input().split()))
    if n * m == 0:
        break
    arr = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(m):
        arr.append(list(map(int, input().split())))
    visited = []
    count = 0
    for i in range(m):
        for j in range(n):
            q = []
            if arr[i][j] == 1:
                count += 1
                q = [(i, j)]
            while q:
                node = q.pop()
                x, y = node
                arr[x][y] = 0
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    try:
                        if 0 <= nx < m and 0 <= ny < n:
                            if arr[nx][ny] == 1:
                                q.append((nx, ny))
                    except:
                        pass
    print(count)