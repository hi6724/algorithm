import math


def sol(arr, loop):
    result = '1'
    sign = [" ", "+", "-"]
    for i in range(1, len(arr)):
        try:
            result += sign[int(loop[i - 1])]
        except:
            result += ' '
        result += str(arr[i])

    if eval(result.replace(" ", "")) == 0:
        print(result)


def make_three(n, length):
    three = []
    while n != 0:
        three.append(n % 3)
        n //= 3
    while len(three) < length:
        three.append(0)
    three.reverse()
    return three


n = int(input())
for i in range(n):
    m = int(input())
    arr = [1]
    three = []
    for i in range(1, m):
        arr.append(i + 1)
        three.append(0)
    for i in range(3**(m - 1)):
        three = make_three(i, m - 1)
        sol(arr, three)
    print()