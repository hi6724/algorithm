from collections import deque

N, M = map(int, input().split(' '))
board = []
movement = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1],
}
for i in range(N):
  row = list(input())
  board.append(row)

index = 0
for i in range(N):
  for j in range(M):
    q = deque()
    q.append([i, j])
    change_list = []
    while q:
      x, y = q.popleft()
      # 루프로 인한 종료
      if type(board[x][y]) != type("D"):
        continue

      nx = x + movement[board[x][y]][0]
      ny = y + movement[board[x][y]][1]
      board[x][y] = index
      change_list.append([x, y])
      # 이전 그룹에 포함되는 경우
      if type(board[nx][ny]) != type("D"):
        for prev_x, prev_y in change_list:
          board[prev_x][prev_y] = board[nx][ny]

        continue
      q.append([nx, ny])

    index += 1

ans = set()
for row in board:
  for el in row:
    ans.add(el)

print(len(ans))
