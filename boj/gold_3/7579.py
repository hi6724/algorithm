from collections import defaultdict

N, M = map(int, input().split(' '))
memories = list(map(int, input().split(' ')))
costs = list(map(int, input().split(' ')))

dp = defaultdict(lambda: defaultdict(int))

for i in range(N):
  memory, cost = memories[i], costs[i]
  for j in range(sum(costs)+1):
    if cost > j:
      dp[i+1][j] = dp[i][j]
      continue
    dp[i+1][j] = max(memory + dp[i][j-cost], dp[i][j])


for key in dp[N]:
  if dp[N][key] >= M:
    print(key)
    break
