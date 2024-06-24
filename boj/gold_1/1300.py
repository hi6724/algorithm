N = int(input())
K = int(input())

def get_count(num):
  tmp = N+1
  count = 0
  if num < tmp:
    tmp = num+1
  for i in range(1,tmp):
    add_num = num//i
    if add_num>N:
      add_num= N
    count+=add_num
  return count

left,right = 1,N**2
while True:
  mid = (left+right)//2
  left_value, mid_value,right_value = get_count(left),get_count(mid), get_count(right)
  if left>right:
    break
  elif mid_value >= K:
    right = mid - 1
  elif mid_value < K:
    left = mid + 1

print(left)