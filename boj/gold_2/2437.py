N = int(input())
weight_list = list(map(int, input().split(' ')))
weight_list.sort()

sum_list = [weight_list[0]]
for i in range(1, N):
  sum_list.append(sum_list[i-1]+weight_list[i])

ans = sum_list[-1] + 1

if weight_list[0] > 1:
  ans = 1
else:
  for i in range(1, N):
    weight = weight_list[i]
    prefix_sum = sum_list[i-1]
    if weight > prefix_sum + 1:
      ans = prefix_sum + 1
      break

print(ans)
