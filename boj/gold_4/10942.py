import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split(" ")))

dp = [[0 for _ in range(N)] for __ in range(N)]

for i in range(len(dp)):
    dp[i][i] = 1

for i in range(1, N):
    for j in range(i, N):
        if nums[j-i] == nums[j]:
            dp[j-i][j] = 1


cnt = 2
for i in range(cnt, N):
    for j in range(i, N):
        if nums[j-i] == nums[j]:
            dp[j-i][j] = dp[j-i+1][j-1]
        else:
            dp[j-i][j] = 0
    cnt += 1


R = int(input())
for i in range(R):
    x, y = map(int, input().split(" "))
    if x > y:
        print(dp[y-1][x-1])
    else:
        print(dp[x-1][y-1])


# 7
# 1 2 1 3 1 2 1
