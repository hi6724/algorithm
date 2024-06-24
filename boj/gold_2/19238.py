from collections import deque
from copy import deepcopy
import math


N, M, fuel = map(int, input().split(' '))
board = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
  row = list(map(int, input().split(' ')))
  board.append(row)

x, y = map(int, input().split(' '))
guests = []

for i in range(M):
  start_x, start_y, end_x, end_y = map(int, input().split(' '))
  guests.append([start_x-1, start_y-1, end_x-1, end_y-1])
guests.sort()


def get_pos(pos, guest_type, guest_index):
  global guests, board
  q = deque([pos])
  new_board = deepcopy(board)
  while len(q) > 0:
    node = q.popleft()
    if len(node) == 0:
      break
    x, y = node
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
        continue
      if new_board[nx][ny] != 0:
        continue
      if nx == pos[0] and ny == pos[1]:
        continue
      new_board[nx][ny] = new_board[x][y] - 1
      q.append([nx, ny])

  max_value = -math.inf
  max_pos = []
  max_index = -1

  if guest_type == "start":
    for i in range(len(guests)):
      guest = guests[i]
      tmp_x, tmp_y = guest[0], guest[1]
      cost = new_board[tmp_x][tmp_y]
      if max_value < cost:
        max_value = cost
        max_pos = [tmp_x, tmp_y]
        max_index = i
      # elif max_value == cost:
      #   temp_list = []
      #   temp_list.append([max_pos[0], max_pos[1], max_index])
      #   temp_list.append([tmp_x, tmp_y, i])
      #   temp_list.sort()
  else:
    guest = guests[guest_index]
    tmp_x, tmp_y = guest[2], guest[3]
    max_value = new_board[tmp_x][tmp_y]
    max_pos = [tmp_x, tmp_y]
    max_index = guest_index
  # for row in new_board:
  #   print(row)
  # print("_________________")
  return [max_pos, max_value, max_index]


cur_pos = [x-1, y-1]
while True:
  # 태울 손님이 없으면 끗
  if len(guests) == 0:
    break

  # 가장 가까운 손님 찾음
  start_pos, cost, guest_index = get_pos(cur_pos, 'start', 0)

  fuel += cost
  if cost == 0:
    if guests[guest_index][0] != cur_pos[0] or guests[guest_index][1] != cur_pos[1]:
      fuel = -1
      break
  if fuel < 0:
    fuel = -1
    break

  end_pos, cost, index = get_pos(start_pos, 'end', guest_index)
  # 못감
  fuel += cost
  if cost == 0:
    if end_pos[0] != start_pos[0] or end_pos[1] != start_pos[1]:
      fuel = -1
      break
  if fuel < 0:
    fuel = -1
    break
  guests.pop(index)
  fuel -= (cost*2)
  cur_pos = deepcopy(end_pos)
  # print(fuel, cost)

if fuel < 0:
  fuel = -1
print(fuel)


'''
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
4 2 3 5
5 4 1 6
2 2 5 6


7 15 9
0 0 0 1 0 0 0
0 0 0 0 1 0 0
0 0 0 0 0 0 0
0 0 1 0 0 0 0
0 1 0 0 1 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
5 6
1 2 2 3
7 3 5 7
3 3 5 6
6 6 3 3
5 6 5 7
4 5 7 3
2 2 3 6
4 4 2 2
7 4 4 7
1 5 6 1
6 2 4 1
1 7 6 1
3 4 5 7
4 2 1 5
4 1 6 3




6 1 2
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
3 4
3 4 3 4


6 1 1
0 0 0 0 1 0
0 0 0 0 1 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1
1 6 1 3
'''
