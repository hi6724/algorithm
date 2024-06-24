from collections import deque
from copy import deepcopy


def sol():
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  dx2 = [1, 1, 2, 2, -1, -1, -2, -2]
  dy2 = [2, -2, 1, -1, 2, -2, 1, -1]

  K = int(input())
  W, H = map(int, input().split(' '))

  tmp = []
  board = []
  for i in range(H):
    income = list(map(int, input().split(' ')))
    row = []
    for el in income:
      if el == 0:
        row.append(el)
      else:
        row.append("*")
    tmp.append(row)

  for i in range(K+1):
    tmp_arr = deepcopy(tmp)
    board.append(tmp_arr)
  if board[0][-1][-1] != 0:
    print(-1)
    return
  if W == 1 and H == 1 and board[0][0][0] == 0:
    print(0)
    return
  start = [0, 0, 0]
  q = deque([start])

  while q:
    [x, y, cnt] = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if nx < 0 or ny < 0 or nx >= H or ny >= W:
        continue
      next_node = board[cnt][nx][ny]

      if next_node == '*':
        continue

      # 첫방문이면
      if board[cnt][nx][ny] == 0:
        board[cnt][nx][ny] = board[cnt][x][y] + 1
        q.append([nx, ny, cnt])
      # 더 작은 값으로 이동 가능하면
      elif board[cnt][nx][ny] > board[cnt][x][y] + 1:
        board[cnt][nx][ny] = board[cnt][x][y] + 1
        q.append([nx, ny, cnt])

    if cnt < K:
      for i in range(8):
        nx, ny = x+dx2[i], y+dy2[i]
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
          continue
        next_node = board[cnt+1][nx][ny]

        if next_node == '*':
          continue

        if board[cnt+1][nx][ny] == 0:
          board[cnt+1][nx][ny] = board[cnt][x][y] + 1
          q.append([nx, ny, cnt+1])

        elif board[cnt+1][nx][ny] > board[cnt][x][y] + 1:
          board[cnt+1][nx][ny] = board[cnt][x][y] + 1
          q.append([nx, ny, cnt+1])

  ans = 999999999999999999

  for bb in board:
    # for row in bb:
    #   print(bb)
    # print("_______________________________")
    if bb[-1][-1] != 0:
      ans = min(ans, bb[-1][-1])

  if ans == 0:
    print(-1)
  elif ans == 999999999999999999:
    print(-1)
  else:
    print(ans)


sol()
