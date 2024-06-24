from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
X, Y = map(int, input().split(' '))
board = []
swans = []
for i in range(X):
  row = list(input())
  board.append(row)

q = deque()
for x in range(X):
  for y in range(Y):
    if board[x][y] == "X":
      board[x][y] = -1
    else:
      if board[x][y] == "L":
        swans.append([x, y])
      board[x][y] = 0
      q.append([x, y])
max_cnt = 0
while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if nx < 0 or ny < 0 or nx >= X or ny >= Y:
      continue
    if board[nx][ny] == -1:
      board[nx][ny] = board[x][y]+1
      max_cnt = max(max_cnt, board[nx][ny])
      q.append([nx, ny])


# 주변 0탐색 -> 없음 -> 주변 1탐색 -> ...
x, y = swans[1]
board[x][y] = -1
# x, y = swans[0]
# board[x][y] = -1
q = [swans[0]]


for i in range(max_cnt+1):
  next_q = set()
  while q:
    x, y = q.pop()
    for j in range(4):
      nx, ny = x+dx[j], y+dy[j]
      if nx < 0 or ny < 0 or nx >= X or ny >= Y:
        continue
      if board[nx][ny] == "L":
        continue
      if board[nx][ny] <= i:
        board[nx][ny] = "L"
        q.append([nx, ny])
      else:
        next_q.add(x*Y + y)
  x, y = swans[1]
  if board[x][y] == "L":
    print(i)
    break
  for el in list(next_q):
    x = el//Y
    y = el % Y
    q.append([x, y])

  # print("______________", i, "________________")
  # for row in board:
  #   print(row)
  # print(next_q)

'''
4 4
..L.
.L..
....
....

8 17
...XXXXXX..XX.XXX
L...XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX..XXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...

'''
