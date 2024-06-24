import math


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


n = int(input())
origin = str(n)
arr = []
for i in str(n):
    if i != '0':
        arr.append(int(i))
temp = arr[0]

for i in range(1, len(arr)):
    temp = lcm(temp, arr[i])
if n % temp == 0:
    print(n)
else:
    i = 1
    cnt = 10
    # 나누어 떨어질 때 까지 반복
    while True:
        num = origin + str(cnt)[1:]
        if int(num) % temp == 0:
            break
        cnt += 1
        if cnt / 10**i == 2:
            cnt = cnt * 10 // 2
            i += 1
    print(num)
