
#i번째줄이 i번째로 도착하는지 판단하는 함수 
def check(): 
    for start in range(N): #모든 시작점에 대해서 
        now = start 
        for j in range(H): 
            if board[j][now]: # 가로선이 오른쪽에 존재한다면
                now += 1 #오른쪽으로이동  
            elif now > 0 and board[j][now - 1]: # 가로선이 왼쪽에 존재한다면
                now -= 1 #왼쪽으로 이동 
        if now != start: #시작위치로 안돌아왔으면  
          return False  #불일치 
    return True


def dfs(cnt, x, y):
    global ans
    if check(): #조건만족하면 
        ans = min(ans, cnt) #최소값 업데이트 후 
        return #종료 
    elif cnt == 3 or ans <= cnt: #횟수가 3넘어가거나 최소값넘어가면
        return #종료 

    for i in range(x, H): #행
        if i == x: # 행이 변경되기 전에는
          now = y #지금 탐색중인 열부터 
        else: # 행이 변경될 경우
          now = 0  #가로선 처음부터 탐색

        for j in range(now, N - 1): #열
            if not board[i][j] and not board[i][j + 1]: #오른쪽에 사다리가 존재하지 않는 경우
                if j > 0 and board[i][j - 1]: # 왼쪽에 사다리가 존재하는 경우는 패스   
                  continue  
                board[i][j] = True 
                dfs(cnt + 1, i, j + 2) 
                board[i][j] = False 


N, M, H = map(int, input().split()) #세로, 사다리, 가로 
board = [[False] * N for _ in range(H)] #사다리배열

for _ in range(M): 
  a, b = map(int, input().split())
  board[a - 1][b - 1] = True #사다리가 있는 곳 

ans = 4 #최대 정답값 
dfs(0, 0, 0) 
print(ans if ans < 4 else -1)