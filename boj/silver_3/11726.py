def sol(n):
    result = [1, 2, 3]
    if n < 4:
        print(n)
        return
    for i in range(3, n):
        result.append(result[i - 1] + result[i - 2])
    print(result[-1] % 10007)


n = int(input())
sol(n)
