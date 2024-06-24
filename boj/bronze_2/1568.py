def sol(N):
    i = 0
    ans = 0
    while N > 0:
        i += 1
        ans += 1
        if N >= i:
            N -= i
        else:
            i = 1
            N -= i
    print(ans)


sol(int(input()))