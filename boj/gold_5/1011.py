import math

n = int(input())


def get_num(num, judge):
    ans = num
    while True:
        temp = ans * (ans + 1)
        if temp < judge:
            ans += 1
        else:
            break
    return ans


for i in range(n):
    x, y = map(int, input().split())
    total = y - x
    temp = math.floor(total**0.5)
    tt = get_num(temp, total)
    prev = tt * (tt - 1)
    current = tt * (tt + 1)
    ans = tt * 2 - 1
    if prev + tt < total:
        ans = tt * 2
    print(ans)
