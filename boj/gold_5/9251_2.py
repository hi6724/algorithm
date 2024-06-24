str1 = list(input())
str2 = list(input())
dp = [[0 for _ in range(len(str2)+1)] for __ in range(len(str1)+1)]

ans = 0
for i in range(1, len(dp)):
    cur = str1[i-1]
    for j in range(1, len(dp[0])):
        next = str2[j-1]
        if cur == next:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if dp[i][j] > ans:
            ans = dp[i][j]


print(ans)
