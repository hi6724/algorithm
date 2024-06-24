string_1 = list(input())
string_2 = list(input())

dp = [[0 for _ in range(len(string_1)+1)] for __ in range(len(string_2)+1)]

for i in range(1, len(string_1)+1):
  for j in range(1, len(string_2)+1):
    if string_1[i-1] == string_2[j-1]:
      dp[j][i] += dp[j-1][i-1]+1
    else:
      dp[j][i] = max(dp[j-1][i], dp[j][i-1])


x, y = [-1, -1]
dx = [-1, 0]
dy = [0, -1]

ans = []
while dp[x][y] > 0:
  moved = False
  for i in range(2):
    nx, ny = x+dx[i], y+dy[i]
    if dp[nx][ny] == dp[x][y]:
      x, y = nx, ny
      moved = True
      continue

  if not moved:
    ans.append(string_1[y])
    x, y = x-1, y-1
ans.reverse()
print(len(ans))
print("".join(ans))
