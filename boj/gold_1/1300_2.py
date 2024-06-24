from collections import defaultdict
N = int(input())
K = int(input())
# 몇번째 수인지 return해주는 함수
def get_count(num):
  global N
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
  left_value,right_value = get_count(left),get_count(right)
  mid=(left+right)//2
  mid_value = get_count(mid)
  

  if mid_value>=K:
    right = mid - 1
  elif mid_value<K:
    left = mid + 1
  if left>right:
    break
  # print(left,right)
print(left)