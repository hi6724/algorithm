from collections import deque
N, M = map(int, input().split(' '))

cheese = []
positions = {}
positions2 = {}
index = 0
index2 = 0
for i in range(N):
  cheese.append(list(map(int, input().split(' '))))

for i in range(N):
  for j in range(M):
    if cheese[i][j] == 1:
      positions[index] = (i, j)
      index += 1
    else:
      positions2[index] = (i, j)
      index += 1

# 치즈 내부 처리


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0

q = deque()
q.append([0, 0])
while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if cheese[nx][ny] == 0:
      cheese[nx][ny] = 2
      q.append([nx, ny])


while positions:

  visited = [[False for i in range(M)] for j in range(N)]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if cheese[nx][ny] != 1 and not visited[nx][ny]:
        cheese[nx][ny] = 2
        visited[nx][ny] = True
        q.append([nx, ny])

  del_arr = []
  for key, (x, y) in positions.items():
    cnt = 0
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if cheese[nx][ny] == 2:
        cnt += 1
    if cnt >= 2:
      del_arr.append(key)

  for del_key in del_arr:
    x, y = positions[del_key]
    cheese[x][y] = 0
    q.append([x, y])
    del positions[del_key]

  time += 1
print(time)

'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
'''
