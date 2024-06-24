board = []
N,M,x,y,R = map(int,input().split(' '))
for i in range(N):
  board.append(list(map(int,input().split(' '))))
commands = list(map(int,input().split(' ')))

dice={
  'front':0,
  'back':0,
  'right':0,
  'left':0,
  'bottom':0,
  'top':0
}

def roll_dice(type):
  global dice,x,y,N,M
  #  동
  if type == 1:
    if y+1 >= M:
      return False
    dice['bottom'],dice['right'],dice['left'],dice['top']  = dice['right'],dice['top'],dice['bottom'],dice['left']
    x,y = x,y+1
  #  서
  elif type == 2:
    if y-1 < 0:
      return False
    dice['bottom'],dice['right'],dice['left'],dice['top']  = dice['left'],dice['bottom'],dice['top'],dice['right']
    x,y = x,y-1
  #  남
  elif type == 3:
    if x-1 < 0:
      return False
    dice['bottom'],dice['front'],dice['back'],dice['top']  = dice['back'],dice['bottom'],dice['top'],dice['front']
    x,y = x-1,y
  #  북
  else:
    if x+1 >= N:
      return False
    dice['bottom'],dice['front'],dice['back'],dice['top']  = dice['front'],dice['top'],dice['bottom'],dice['back']
    x,y = x+1,y
  return True


def change_num(x,y):
  global dice,board
  if board[x][y]==0:
    board[x][y] = dice['bottom']

  else:
    dice['bottom']=board[x][y]
    board[x][y]=0



for command in commands:
  if roll_dice(command):
    change_num(x,y)
    print(dice['top'])

