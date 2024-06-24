N, K = list(map(int, input().split()))
coins = []
for i in range(N):
    coins.append(int(input()))
ans = 0
while coins:
    coin = coins.pop()
    while K >= coin:
        K = K - coin
        ans += 1
print(ans)