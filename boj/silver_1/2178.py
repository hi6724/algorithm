from collections import deque

N, M = map(int, input().split())
maze_list = []
for i in range(N):
    maze = list(input())
    maze_list.append(maze)
maze_list[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = [[0, 0]]

while q:
    x, y = q[0][0], q[0][1]
    del q[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if maze_list[nx][ny] == '1':
                q.append([nx, ny])
                maze_list[nx][ny] = maze_list[x][y] + 1
print(maze_list[N - 1][M - 1])
