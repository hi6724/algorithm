n, r, c = list(map(int, input().split()))
ans = 0
while n > 1:
    n -= 1
    d = 2**n
    if c < d:
        if r < d:
            pass
        else:
            ans += d * d * 2
            r -= d
    else:
        if r < d:
            ans += d * d
            c -= d
        else:
            ans += d * d * 3
            r -= d
            c -= d
ans += r + c
if r == 1 and c == 1:
    ans += 1
if c == 0 and r == 1:
    ans += 1
print(ans)
