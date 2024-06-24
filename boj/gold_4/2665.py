import heapq

def check_range(y, x):
  return (0 <= y < N) and (0 <= x < N)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().strip())))

q=[]
visited = [[0 for _ in range(N)] for _ in range(N)]
heapq.heappush(q,(0,0,0))
visited[0][0]=1
ans=0

while q:
  weight,x,y = heapq.heappop(q)
  if x == N-1 and y == N-1:
    ans=weight
    break
  
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if check_range(nx,ny) and visited[nx][ny]==0:
      visited[nx][ny]=1
      if board[nx][ny]==1:
        heapq.heappush(q,(weight,nx,ny))
      else:
        heapq.heappush(q,(weight+1,nx,ny))

print(ans)