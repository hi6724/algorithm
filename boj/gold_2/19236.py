from copy import deepcopy

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
ans = -1


def dfs(board, pos_dict, score, direction, pos):
  global ans
  # 물고기 이동
  for key in range(1, 17):
    fish_x, fish_y = pos_dict[key]
    if fish_x == -1:
      continue
    fish_id, fish_dir = board[fish_x][fish_y]
    while True:
      fish_nx, fish_ny = fish_x+dx[fish_dir], fish_y+dy[fish_dir]
      if fish_nx < 0 or fish_ny < 0 or fish_nx >= 4 or fish_ny >= 4:
        if fish_dir < 8:
          fish_dir = fish_dir + 1
        else:
          fish_dir = 1
      elif board[fish_nx][fish_ny][0] == -1:
        if fish_dir < 8:
          fish_dir = fish_dir + 1
        else:
          fish_dir = 1
      else:
        next_fish_id, next_fish_dir = board[fish_nx][fish_ny]
        board[fish_nx][fish_ny] = [fish_id, fish_dir]
        board[fish_x][fish_y] = [next_fish_id, next_fish_dir]
        pos_dict[fish_id] = [fish_nx, fish_ny]
        pos_dict[next_fish_id] = [fish_x, fish_y]
        break

  for i in range(1, 4):
    x, y, = pos
    nx, ny = x + (dx[direction]*i), y + (dy[direction]*i)
    if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
      ans = max(ans, score)

      # for row in board:
      #   print(row)
      continue
    elif board[nx][ny][0] == 0:
      ans = max(ans, score)

      # for row in board:
      #   print(row)
      continue
    new_board = deepcopy(board)
    new_pos_dict = deepcopy(pos_dict)
    new_pos_dict[new_board[nx][ny][0]] = [-1, -1]
    new_score, new_dir = score + new_board[nx][ny][0], new_board[nx][ny][1]
    new_board[nx][ny] = [-1, -1]
    new_board[x][y] = [0, 0]

    dfs(new_board, new_pos_dict, new_score, new_dir, [nx, ny])


board = []
for i in range(4):
  data = list(map(int, input().split(' ')))
  row = []
  for j in range(4):
    row.append(data[j*2:(j+1)*2])
  board.append(row)

pos_dict = {}
for x in range(4):
  for y in range(4):
    _id = board[x][y][0]
    pos_dict[_id] = [x, y]

init_score = board[0][0][0]
init_direction = board[0][0][1]
board[0][0] = [-1, -1]
pos_dict[init_score] = [-1, -1]


dfs(board, pos_dict, init_score, init_direction, [0, 0])
print(ans)
