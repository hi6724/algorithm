def sol(N):
    count_3 = 0
    count_5 = 0
    while N > 0:
        if N % 5 == 0:
            count_5 = N // 5
            N = 0
        elif N < 3:
            return -1
        else:
            count_3 += 1
            N -= 3
    return (count_3 + count_5)


N = int(input())
print(sol(N))