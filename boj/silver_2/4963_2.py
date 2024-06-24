
dx= [1,1,1,0,-1,-1,-1,0]
dy=[1,0,-1,-1,-1,0,1,1]
while True:
    cnt=0
    n,m=(map(int,input().split(' ')))
    if n+m==0:
        break
    arr=[]
    for i in range(m):
        temp=input().split(' ')
        arr.append(temp)
    for i in range(m):
        for j in range(n):
            if arr[i][j]=="1":
                cnt+=1
                q=[(i,j)]
                while q:
                    x,y=q.pop()
                    for d in range(8):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if 0<=nx<m and 0<=ny<n:
                            if arr[nx][ny]=='1':
                                q.append((nx,ny))
                                arr[nx][ny]='0' 
    print(cnt)