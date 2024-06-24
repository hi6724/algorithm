import math
from itertools import combinations


prime_ox = [True for _ in range(4000001)]

for i in range(2, int(4000001 ** 0.5)):
  if prime_ox[i]:
    for j in range(i+i, 4000001, i):
      prime_ox[j] = False
prime_list = [i for i, j in enumerate(prime_ox) if j == True and i >= 2]

sum_prime = [0] * (len(prime_list) + 1)
for i in range(len(prime_list)):
  sum_prime[i+1] = sum_prime[i] + prime_list[i]

N = int(input())

answer = 0
start = 0
end = 1

while start < len(sum_prime) and prime_list[end-1] <= N:
    if sum_prime[end] - sum_prime[start] == N:  # 소수와 같을 경우
        answer += 1
        start += 1
    elif sum_prime[end] - sum_prime[start] > N:  # 소수보다 클 경우 start += 1
        start += 1
    else:
        if end < len(sum_prime) - 1:  # 소수보다 작을 경우 end += 1
            end += 1
        else:
            start += 1

print(answer)
