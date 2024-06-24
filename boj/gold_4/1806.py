import math
N, target = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr_sum = [0]
for el in range(N):
  arr_sum.append(arr_sum[-1]+arr[el])
left, right = 0, 0
ans = math.inf
while True:
  if arr_sum[right]-arr_sum[left] >= target:
    ans = min(ans, right-left)
    left += 1
  elif right == N:
    break
  else:
    right += 1

if ans == math.inf:
  print(0)
else:
  print(ans)
