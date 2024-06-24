from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, T = map(int, input().split(' '))

boards = []
cleaner = []
for i in range(N):
  boards.append(list(map(int, input().split(' '))))
for i in range(N):
  for j in range(M):
    if boards[i][j] == -1:
      cleaner.append([i, j])
for t in range(T):

  # 확산 1 사이클 여기 틀림
  temp = []
  for i in range(N):
    for j in range(M):
      if boards[i][j] > 0:
        temp.append([i, j, boards[i][j]])

  for i, j, value in temp:
    cnt = 0
    for d in range(4):
      nx = i+dx[d]
      ny = j+dy[d]
      if nx < 0 or nx >= N or ny < 0 or ny >= M or boards[nx][ny] == -1:
        continue
      boards[nx][ny] += value//5
      cnt += 1
    boards[i][j] -= (value//5)*cnt
  total = 0

  # 공기 청정기 1 사이클
  # 공기 청정기 위
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  direct = 0
  x, y = cleaner[0][0], 1
  prev = 0
  while True:
    nx, ny = x+dx[direct], y+dy[direct]
    if x == cleaner[0][0] and y == 0:
      break
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      direct += 1
      continue
    boards[x][y], prev = prev, boards[x][y]
    x, y = nx, ny

  # 공기 청정기 밑
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  direct = 0
  x, y = cleaner[1][0], 1
  prev = 0
  while True:
    nx, ny = x+dx[direct], y+dy[direct]
    if x == cleaner[1][0] and y == 0:
      break
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      direct += 1
      continue
    boards[x][y], prev = prev, boards[x][y]
    x, y = nx, ny

ans = 0
for i in range(N):
  ans += sum(boards[i])
print(ans+2)
