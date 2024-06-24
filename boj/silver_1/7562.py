from collections import deque

repeat = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for i in range(repeat):
    N = int(input())
    now_pos = list(map(int, input().split()))
    target_pos = list(map(int, input().split()))
    arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    q = deque()
    q.append(now_pos)
    arr[now_pos[0]][now_pos[1]] = 1
    while q:
        x, y = q.popleft()
        if x == target_pos[0] and y == target_pos[1]:
            print(arr[x][y] - 1)
            q = deque()
            break
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append([nx, ny])
