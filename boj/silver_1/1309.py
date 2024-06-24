# https://www.acmicpc.net/problem/1309

n = int(input())
dp = [1, 3]
for i in range(2, n + 1):
    temp = dp[i - 1] * 2 + dp[i - 2]
    dp.append(temp%9901)

print(dp[n]%9901)
