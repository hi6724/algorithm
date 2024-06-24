N, k = map(int, input().split(" "))
nums = [int(input()) for _ in range(N)]
dp = [0 for _ in range(k+1)]
dp[0] = 1


for num in nums:
    for i in range(num, k+1):
        if i-num >= 0:
            dp[i] += dp[i-num]
print(dp[k])
