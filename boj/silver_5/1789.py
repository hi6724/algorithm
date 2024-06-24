n = int(input())

ans = 0
temp = 1
while temp <= n:
    temp = ((1 + ans) * (ans)) / 2
    ans += 1
print(ans - 2)
