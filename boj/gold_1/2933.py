from collections import deque, defaultdict
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
X, Y = map(int, input().split(' '))
board = []

for i in range(X):
  row = []
  temp = list(input())
  for el in temp:
    if el == 'x':
      row.append(0)
    else:
      row.append(-1)
  board.append(row)
N = int(input())
stones = list(map(int, input().split(' ')))

for i in range(len(stones)):

  # 돌 지우기
  stone = -stones[i]
  if i % 2 == 0:
    for j in range(len(board[0])):
      if board[stone][j] == 0:
        board[stone][j] = -1
        break
  else:
    for j in range(-1, -len(board[0])-1, -1):
      if board[stone][j] == 0:
        board[stone][j] = -1
        break

  # 클러스터링
  new_board = deepcopy(board)
  clusters = defaultdict(list)
  for i in range(len(board)):
    for j in range(len(board[0])):
      if new_board[i][j] != 0:
        continue
      new_board[i][j] = i*100+j + 10
      clusters[i*100+j+10].append([i, j])
      q = deque([[i, j]])
      while q:
        x, y = q.popleft()
        for d in range(4):
          nx, ny = x+dx[d], y+dy[d]
          if nx < 0 or ny < 0 or nx >= X or ny >= Y:
            continue
          if new_board[nx][ny] != 0:
            continue
          value = new_board[x][y]
          clusters[value].append([nx, ny])
          new_board[nx][ny] = new_board[x][y]
          q.append([nx, ny])

  # 각각의 클러스터의 가장 아래 노드가 바닥인지 확인
  # print(clusters)
  # print("_______________________________________")
  # for row in new_board:
  #   print(row)
  for key in clusters:
    clusters[key].sort(key=lambda x: -x[0])
    # print(clusters[key])
    if clusters[key][0][0] == X-1:
      continue
    cnt = 1
    while True:
      tagets = clusters[key]
      is_ok = True
      if cnt+tagets[0][0] == X-1:
        if new_board[X-1][tagets[0][1]] != -1:
          cnt -= 1
        break

      for el in tagets:
        x, y = el

        if new_board[x+cnt][y] != -1 and new_board[x+cnt][y] != key:
          cnt -= 1
          is_ok = False
          break
      if not is_ok:
        break
      cnt += 1

    for el in clusters[key]:
      x, y = el
      new_board[x][y] = -1
      new_board[x+cnt][y] = key

  for x in range(len(new_board)):
    for y in range(len(row)):
      if new_board[x][y] == -1:
        board[x][y] = -1
      else:
        board[x][y] = 0


for row in board:
  for el in row:
    result = '.'
    if el == 0:
      result = 'x'
    print(result, end='')
  print()
