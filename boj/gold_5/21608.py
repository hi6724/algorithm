from collections import defaultdict

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
total_prefer_list = defaultdict(list)
order = []
seat_dict = defaultdict(list)


for i in range(N**2):
  [a, b, c, d, e] = list(map(int, input().split(' ')))
  total_prefer_list[a] = [b, c, d, e]
  order.append(a)

board[1][1] = order[0]
seat_dict[order[0]] = [1, 1]

for index in range(1, len(order)):
  person = order[index]
  prefer_list = total_prefer_list[person]
  tmp = set()

  for prefer in prefer_list:
    prefer_seat = seat_dict[prefer]
    if len(prefer_seat) > 0:
      prefer_x, prefer_y = prefer_seat
      for i in range(4):
        nx = prefer_x+dx[i]
        ny = prefer_y+dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if board[nx][ny] != 0:
          continue
        tmp.add(nx*N+ny)

  max_score = 0
  empty_score = -1
  result_seat = []

  for i in range(N**2):
    x, y = i//N, i % N
    tmp_empty_score = 0
    if board[x][y] != 0:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if board[nx][ny] == 0:
        tmp_empty_score += 1
    if tmp_empty_score > empty_score:
      result_seat = [x, y]
      empty_score = tmp_empty_score
  tmp = list(tmp)
  tmp.sort()
  for pos in tmp:
    tmp_score = 0
    tmp_empty_score = 0
    x, y = pos//N, pos % N
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if board[nx][ny] in prefer_list:
        tmp_score += 1
      if board[nx][ny] == 0:
        tmp_empty_score += 1
    if tmp_score > max_score:
      max_score = tmp_score
      empty_score = tmp_empty_score
      result_seat = [x, y]
    if tmp_score == max_score and tmp_empty_score > empty_score:
      empty_score = tmp_empty_score
      result_seat = [x, y]

  x, y = result_seat
  board[x][y] = person
  seat_dict[person] = [x, y]


score = 0
for square in range(N**2):
  x, y = square // N, square % N
  person = board[x][y]
  prefer_list = total_prefer_list[person]
  count = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
      continue
    if board[nx][ny] in prefer_list:
      count += 1
  if count > 0:
    score += 10**(count-1)
print(score)
