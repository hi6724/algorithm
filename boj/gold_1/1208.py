from itertools import product
from bisect import bisect_left, bisect_right
import math
# N <=40
# -1,000,000 <= S <=1,000,000


N, S = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

arr1 = arr[:math.ceil(N/2)]
arr2 = arr[math.ceil(N/2):]

sum1 = []
sum2 = []

for i in range(2**len(arr1)):
  base = bin(i).split('b')[1]
  while len(base) < len(arr1):
    base = '0'+base
  sum = 0
  for j in range(len(arr1)):
    if base[j] == '0':
      sum += arr1[j]
  sum1.append(sum)


for i in range(2**(len(arr2))):
  base = bin(i).split('b')[1]
  while len(base) < len(arr2):
    base = '0'+base
  sum = 0
  for j in range(len(arr2)):
    if base[j] == '0':
      sum += arr2[j]
  sum2.append(sum)
sum1_arr = list(sum1)
sum2_arr = list(sum2)

sum1_arr.sort()
sum2_arr.sort()
ans = 0


for l in sum1_arr:
  find = S-l
  ans += bisect_right(sum2_arr, find) - bisect_left(sum2_arr, find)


if S == 0:
  ans -= 1
print(ans)

# print("HHHH")
# arr = [1, 2, 3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 10]
# print(len(arr))
# print(binary_search_right(arr, 7))
# print(binary_search_left(arr, 7))
