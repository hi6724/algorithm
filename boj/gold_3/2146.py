from collections import deque
from itertools import combinations
from copy import deepcopy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
board = []
for i in range(N):
  row = list(map(int, input().split(' ')))
  board.append(row)

lands = set()
for i in range(N):
  for j in range(N):
    if board[i][j] == 0:
      continue
    index = (i*N + j + 1)*N**2

    q = deque()
    if board[i][j] == 1:
      q.append([i, j])
      board[i][j] = index
      lands.add(index)

    while q:
      [x, y] = q.pop()
      for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if board[nx][ny] == 0 or board[nx][ny] == index:
          continue
        if board[nx][ny] == 1:
          board[nx][ny] = index
          q.append([nx, ny])


ans = N**2
for el in lands:
  tmp_board = deepcopy(board)
  q = deque([])
  for i in range(N):
    for j in range(N):
      if tmp_board[i][j] == el:
        q.append([i, j])

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx, ny = x+dx[d], y+dy[d]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue

      if tmp_board[nx][ny] == 0:
        tmp_board[nx][ny] = tmp_board[x][y] + 1
        q.append([nx, ny])
      elif tmp_board[nx][ny] > tmp_board[x][y]+N**2 or tmp_board[nx][ny] < tmp_board[x][y]-N**2:
        ans = min(ans, tmp_board[x][y]-el)
        q = deque()
        break


print(ans)

'''
10
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
'''
