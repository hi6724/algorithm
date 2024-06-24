N = int(input())


nums = list(map(int, input().split(" ")))
ans = -1001
dp1 = [-1001 for _ in range(N+1)]
dp2 = [-1001 for _ in range(N+1)]

# 제거하지 않은 경우
for i in range(N):
    dp1[i] = max(dp1[i-1]+nums[i], nums[i])
    if dp1[i] > ans:
        ans = dp1[i]
dp2[0] = dp1[0]
for i in range(1, N):
    dp2[i] = max(nums[i]+dp2[i-1], dp1[i-1])
    if dp2[i] > ans:
        ans = dp2[i]
print(ans)
