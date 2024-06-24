# 최대크기 10000 x 10000 => 1억
# 1칸 1칸, 2칸 2칸, 3칸 3칸 ...
from collections import deque

CENTER=5000
dx=[0,-1,0,1]
dy=[1,0,-1,0]


r1,c1,r2,c2 = map(int,input().split(' '))
board = [[0 for i in range(c2-c1 +1)] for i in range(r2- r1 +1)]

direction = 0
index = 2
loop = 1
x,y = 5000,5000
if r1 <= x - 5000 <= r2 and c1 <= y - 5000 <= c2 :
  board[x-5000 - r1][y-5000 - c1]=1

while index<10001*10001:
  direction = direction%4
  for i in range(2):
    for j in range(loop):
      x = x + dx[direction]
      y = y + dy[direction]
      if r1 <= x - 5000 <= r2 and c1 <= y - 5000 <= c2 :
        board[x-5000 - r1][y-5000 - c1]=index
      index+=1
    direction+=1
  loop+=1

max_value = -1
for row in board:
  max_value=max(max_value,max(row))
max_len = len(str(max_value))

for row in board:
  for el in row:
    print(f'%{max_len}.0f' %el,end=' ')
  print()


