from collections import deque

move= [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, -1], [1, 1], [-1, 1]]
def qqq(a,b):
    myque=deque()
    myque.append([a,b])
    while myque: 
        n,m=myque.popleft()
        for i in range (8):
            x=n+move[i][0]
            y=m+move[i][1]
            if 0<=x<h and 0<=y<w and maps[x][y]==1:
                myque.append([x,y])
                maps[x][y]=0

while True:
    w,h=map(int,input().split())
    maps=[]
    answer=0
    if w==0 and h==0:
        break
    for i in range(h):
        maps.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if maps[i][j]==1:
                qqq(i,j)
                answer+=1
    print(answer)