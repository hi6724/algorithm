N = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

boards = []
indexLists = []
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):

    tempList = (list(map(int, input().split(" "))))
    tempList2 = []
    for j in range(len(tempList)):
        indexLists.append([tempList[j], i, j])
    boards.append(tempList)

indexLists.sort(reverse=True)

for indexList in indexLists:
    currentValue = indexList[0]
    x = indexList[1]
    y = indexList[2]
    maxValue = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        if boards[nx][ny] > currentValue:
            if dp[nx][ny]+1 > maxValue:
                maxValue = dp[nx][ny]+1
    dp[x][y] = maxValue

ans = 0
for d in dp:
    if max(d) > ans:
        ans = max(d)

print(ans+1)
