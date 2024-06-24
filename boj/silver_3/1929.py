import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


prime_nums = []
x, y = map(int, input().split(' '))
for i in range(x, y+1):
    if is_prime(i):
        prime_nums.append(i)
for num in prime_nums:
    print(num)
