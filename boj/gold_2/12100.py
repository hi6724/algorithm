# n 진수
def n_bin(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
# move


def move(i, board):
    newBoard = [item[:] for item in board]
    return newBoard


# 5번 이동했을 때 최댓값
# 상 하 좌 우 로 이동하므로 4^5 = 1024 완탐
N = int(input())


rootBoard = []
for i in range(N):
    rootBoard.append(list(map(int, input().split(' '))))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

maxValue = 0
for i in range(1, 4**5):

    board = [item[:] for item in rootBoard]

    cnt = 0
    temp1 = ''
    temp = n_bin(i, 4)
    for i in range(5-len(temp)):
        temp1 += '0'
    temp = temp1+temp

    for i in range(5):
        moveIndex = temp[i]
        # UP
        if moveIndex == '0':
            for y in range(N):
                x = 0
                for _ in range(N):
                    cnt = 1
                    while True:
                        if board[x][y] == 0:
                            for nx in range(x, N-1):
                                board[nx][y] = board[nx+1][y]
                            x -= 1
                            board[N-1][y] = 0
                            break
                        elif x+cnt >= N:
                            break
                        elif board[x][y] == board[x+cnt][y]:
                            board[x][y] = board[x][y]*2
                            board[x+cnt][y] = 0
                            break
                        elif board[x+cnt][y] == 0:
                            cnt += 1
                        else:
                            break
                    x += 1
        # DOWN
        elif moveIndex == '1':
            for y in range(N):
                x = -1
                for _ in range(N):
                    cnt = 1
                    while True:
                        if board[x][y] == 0:
                            for nx in range(x, -N, -1):
                                board[nx][y] = board[nx-1][y]
                            x += 1
                            board[-N][y] = 0
                            break
                        elif x-cnt < -N:
                            break
                        elif board[x][y] == board[x-cnt][y]:
                            board[x][y] = board[x][y]*2
                            board[x-cnt][y] = 0
                            break
                        elif board[x-cnt][y] == 0:
                            cnt += 1
                        else:
                            break
                    x -= 1

        # RIGHT
        elif moveIndex == '2':
            for x in range(N):
                y = -1
                for _ in range(N):
                    cnt = 1
                    while True:
                        if board[x][y] == 0:
                            for ny in range(y, -N, -1):
                                board[x][ny] = board[x][ny-1]
                            y += 1
                            board[x][-N] = 0
                            break
                        elif y-cnt < -N:
                            break
                        elif board[x][y] == board[x][y-cnt]:
                            board[x][y] = board[x][y]*2
                            board[x][y-cnt] = 0
                            break
                        elif board[x][y-cnt] == 0:
                            cnt += 1
                        else:
                            break
                    y -= 1
        # LEFT
        elif moveIndex == '3':
            for x in range(N):
                y = 0
                for _ in range(N):
                    cnt = 1
                    while True:
                        if board[x][y] == 0:
                            for ny in range(y, N-1):
                                board[x][ny] = board[x][ny+1]
                            y -= 1
                            board[x][N-1] = 0
                            break
                        elif y+cnt >= N:
                            break
                        elif board[x][y] == board[x][y+cnt]:
                            board[x][y] = board[x][y]*2
                            board[x][y+cnt] = 0
                            break
                        elif board[x][y+cnt] == 0:
                            cnt += 1
                        else:
                            break
                    y += 1

    for i in range(len(board)):
        maxValue = max(max(board[i]), maxValue)

print(maxValue)

