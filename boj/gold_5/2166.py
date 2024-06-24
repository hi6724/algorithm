N = int(input())
a_list = []
b_list = []

for i in range(N):
  a, b = map(int, input().split(' '))
  a_list.append(a)
  b_list.append(b)
a_list.append(a_list[0])
b_list.append(b_list[0])

a_sum = 0
b_sum = 0

for i in range(N):
  a_sum += a_list[i]*b_list[i+1]
  b_sum += b_list[i]*a_list[i+1]

ans = round(abs(a_sum-b_sum)/2, 1)
print(ans)
