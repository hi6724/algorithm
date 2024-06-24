
board=[]
N,M = map(int,input().split(' '))
x,y,d = map(int,input().split(' '))

# 북, 동, 남, 서
for i in range(N):
  row = list(map(int,input().split(' ')))
  board.append(row)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
  # 1. 현재 칸을 청소한다.
  if board[x][y]== 0:
    board[x][y] = -1

  is_clean = True
  for i in range(4):
    nx,ny = x+dx[i],y+dy[i]
    if board[nx][ny] == 0:
      is_clean = False

  # 2. 4칸 중 0이 없는 경우.
  if is_clean:
    nx = x - dx[d]
    ny = y - dy[d]
    # 2-1. 후진 O
    if board[nx][ny] != 1:
      x,y = nx,ny
    # 2-2. 후진 X
    else:
      break

  # 3. 4칸 중 0이 있는경우.
  else:
    # 3-1. 반시계 방향으로 회전
    d -= 1
    if d < 0:
      d+=4
    # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 경우 전진
    nx = x + dx[d]
    ny = y + dy[d]
    if board[nx][ny] == 0:
      x,y = nx,ny


cnt = 0
for row in board:
  for el in row:
    if el < 0:
      cnt+=1
print(cnt)
