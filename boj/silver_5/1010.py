def sol(n, m):
    for _ in range(n):
        item = []
        for i in range(m):
            item.append(i + 1)
        result.append(item)
    if n == 1:
        pass
    for i in range(n):
        for j in range(m):
            if i > 0:
                temp = 0
                for k in range(0, j):
                    temp += result[i - 1][k]
                result[i][j] = temp

    print(result[-1][-1])


l = int(input())
for i in range(l):
    result = []
    n, m = map(int, input().split(" "))
    sol(n, m)
