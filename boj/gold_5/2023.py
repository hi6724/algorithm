import math


def is_prime_number(x):
    x = int(x)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def sol(n):
    ans = [2, 3, 5, 7]
    if n == 1:
        for i in ans:
            print(i)
        return
    r = 1
    while True:
        temp = []
        for i in ans:
            for j in range(10):
                temp_num = str(i) + str(j)
                if is_prime_number(temp_num):
                    temp.append(int(temp_num))
        ans = temp
        r += 1
        if r == n:
            break
    for i in ans:
        print(i)
    return


n = int(input())
sol(n)