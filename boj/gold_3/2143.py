from itertools import combinations
from bisect import bisect_left, bisect_right
# N <=40
# -1,000,000 <= S <=1,000,000

target = int(input())
N = int(input())
arr1 = list(map(int, input().split(' ')))
M = int(input())
arr2 = list(map(int, input().split(' ')))

# 1차원 누적합 배열 생성 
sum1 = [arr1[0]]
sum2 = [arr2[0]]
for i in range(1, N):
  sum1.append(sum1[-1]+arr1[i])
for i in range(1, M):
  sum2.append(sum2[-1]+arr2[i])

sum1_arr = []
sum1_arr.extend(arr1)
sum2_arr = []
sum2_arr.extend(arr2)
# 모든 부 배열의 합 배열
for start, end in list(combinations(range(N), 2)):
  sum1_arr.append(sum1[end]-sum1[start]+arr1[start])
for start, end in list(combinations(range(M), 2)):
  sum2_arr.append(sum2[end]-sum2[start]+arr2[start])
sum1_arr.sort()
sum2_arr.sort()
ans = 0


for l in sum1_arr:
  find = target-l
  ans += bisect_right(sum2_arr, find) - bisect_left(sum2_arr, find)
print(ans)
