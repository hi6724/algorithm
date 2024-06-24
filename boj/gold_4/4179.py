from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

N,M=map(int,input().split(' '))
boards=[]
q=deque()
for i in range(N):
    boards.append(list(input()))
ans=10000000

for x in range(N):
    for y in range(M):
        if boards[x][y]=="J":
            boards[x][y]=1
            if x==0 or y==0 or x==N-1 or y==M-1:
                ans=1
            q.append([x,y,0])
for x in range(N):
    for y in range(M):
        if boards[x][y]=="F":
            q.append([x,y,0])
while q:
    x,y,index=q.popleft()
    current = boards[x][y]
    stop=False
    endIndex=9999999
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if type(current)==int:
            if boards[nx][ny]==".":
                boards[nx][ny]=current+1
                q.append([nx,ny,index+1])
                if nx==0 or ny==0 or nx==N-1 or ny==M-1:
                    if current+1<ans:
                        endIndex=index
                        stop=True
                        break
        elif current=="F":
            if boards[nx][ny]!="F" and boards[nx][ny]!="#":
                boards[nx][ny]="F"
                q.append([nx,ny,index+1])
    if stop:
        break
newQueue=deque()
for i in range(len(q)):
    if q[i][-1]==endIndex:
        newQueue.append(q[i])
while newQueue:
    x,y,i = newQueue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        boards[nx][ny]="F"

for i in range(len(boards)):
    for j in range(len(boards[0])):
        if i==0 or j==0 or i==N-1 or j==M-1:
            if type(boards[i][j])==int:
                ans=min(boards[i][j],ans)

if ans ==10000000:
    print("IMPOSSIBLE")
elif ans>0:
    print(ans)
else:
    print("IMPOSSIBLE")

# 반례 1. 처음부터 탈출했을때 (ok)
# 반례 2. 탈출하는 타이밍에 불에 닿았을 때