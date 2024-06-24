# from collections import deque

# def is_diamond(board,x,y,step):
#   # start 에서 왼좌 우좌로 내려가면서 체크
#   if board[x][y] == 0:
#     return False
#   if board[x][y] == 1 and step == 1:
#     return True

#   start_x,start_y = x,y
#   for i in range(1,step):
#     if start_x+i >= len(board) or start_y+i >= len(board[0]) or start_y-i <0:
#       return False
#     if board[start_x+i][start_y+i] == 0:
#       return False
#     if board[start_x+i][start_y-i] == 0:
#       return False
#   # 가장 아래에서 왼좌 우좌로 올라오면서 체크

#   end_x,end_y = x+((step-1)*2) ,y
#   if end_x >= len(board):
#     return False
#   if board[end_x][end_y] == 0:
#     return False
#   for i in range(1,step):
#     if end_y+i >= len(board[0]) or end_y-i <0:
#       return False
#     if board[end_x-i][end_y+i] == 0:
#       return False
#     if board[end_x-i][end_y-i] == 0:
#       return False
#   i = 1
#   return True



# R,C = map(int,input().split(' '))
# board = []
# for i in range(R):
#   row = list(map(int,list(input())))
#   board.append(row)

# for x in range(R):
#   for y in range(C):
#     step = board[x][y]
#     while True:
#       is_ok = is_diamond(board,x,y,step)
#       if is_ok:
#         start_x,start_y = x,y
#         end_x,end_y = x+((step-1)*2) ,y
#         for i in range(step):
#           board[start_x+i][start_y+i] = max(board[start_x+i][start_y+i],step)
#           board[start_x+i][start_y-i] = max(board[start_x+i][start_y-i],step)
#           board[end_x-i][end_y+i] = max(board[end_x-i][end_y+i],step)
#           board[end_x-i][end_y-i] = max(board[end_x-i][end_y-i],step)
#         step +=1
#       else:
#         break



# ans = -1
# for row in board:
#   ans = max(ans,max(row))
# print(ans)

n, m = map(int, input().split())
board = [[0] * (m+2) for _ in range(n+2)]

for i in range(1,n+1):
    s = input()
    for j in range(1,m+1):
        board[i][j] = int(s[j-1])

ld = [[0] * (m+2) for _ in range(n+2)]
rd = [[0] * (m+2) for _ in range(n+2)]
lu = [[0] * (m+2) for _ in range(n+2)]
ru = [[0] * (m+2) for _ in range(n+2)]

for i in range(n, 0, -1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            ld[i][j] = ld[i+1][j-1] + 1
            rd[i][j] = rd[i+1][j+1] + 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            lu[i][j] = lu[i-1][j-1] + 1
            ru[i][j] = ru[i-1][j+1] + 1

result = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        l = result if result != 0 else 1
        for k in range(l, min(ld[i][j], rd[i][j])+1):
            t = i + (k-1)*2
            if t > n+1:
                break
            if board[t][j] and lu[t][j] >= k and ru[t][j] >=k:
                result = k
        for k in range(l, min(rd[i][j], ru[i][j])+1):
            t = j + (k-1)*2
            if t > m+1:
                break
            if board[i][t] and lu[i][t] >= k and ld[i][t] >=k:
                result = k
print(result)