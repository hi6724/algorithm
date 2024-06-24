# 백준 5585
coins = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
ans = 0
for coin in coins:
    if n >= coin:
        ans += n // coin
        n -= (coin * (n // coin))

print(ans)