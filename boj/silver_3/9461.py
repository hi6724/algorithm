def sol(n):
    result = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n < 10:
        print(result[n - 1])
        return
    for i in range(10, n):
        # print(i - 1, i - 5)
        result.append(result[i - 1] + result[i - 5])
    print(result[-1])


for i in range(int(input())):
    sol(int(input()))
