n = int(input())
ans = [0] * (n + 1)
dp = []
for i in range(n):
    r, g, b = map(int, input().split())
    dp.append([r, g, b])
for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 2]) + dp[i][j]
print(min(dp[-1]))