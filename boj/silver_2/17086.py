from collections import deque

dx=[-1,-1,-1,1,1,1,0,0]
dy=[-1,1,0,-1,1,0,1,-1]

N,M=map(int,input().split(' '))
boards=[]
sharks=[]
q=deque()
for i in range(N):
    boards.append(list(map(int,input().split(' '))))

for x in range(N):
    for y in range(M):
        if boards[x][y]==1:
            q.append([x,y])
            sharks.append([x,y])

while q:
    x,y=q.popleft()
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if boards[nx][ny]==0:
            boards[nx][ny]+=boards[x][y]+1
            q.append([nx,ny])

maxValue=-1

for board in boards:
    if max(board)>maxValue:
        maxValue=max(board)
print(maxValue-1)