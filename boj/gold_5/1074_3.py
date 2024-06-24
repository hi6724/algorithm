def sol(n, x, y):
    global result
    r = 2**n
    if n == 1:
        result += (y - 1) * 2 + (x - 1)
        print(int(result))
        return
    if x > 2**(n - 1) and y > 2**(n - 1):
        result += r * r * 3 / 4
        x -= 2**(n - 1)
        y -= 2**(n - 1)
    elif y > 2**(n - 1):
        result += r * r * 2 / 4
        y -= 2**(n - 1)
    elif x > 2**(n - 1):
        result += r * r * 1 / 4
        x -= 2**(n - 1)

    sol(n - 1, x, y)


result = 0
N, Y, X = map(int, input().split(" "))
X = X + 1
Y = Y + 1
sol(N, X, Y)