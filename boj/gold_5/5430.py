from collections import deque

T = int(input())
for t in range(T):
  commands = input()
  n = input()
  temp = input()
  is_reverse = False
  nums_list=[]
  if int(n) > 0:
    nums_list = list(map(int,temp[1:-1].split(',')))
  q = deque(nums_list)
  is_error=False
  for command in commands:
    if command == "R":
      is_reverse = not is_reverse
    if command == "D":
      if len(q)>0:
        if is_reverse:
          q.pop()
        else:
          q.popleft()
      else:
        is_error=True

  if is_error:
    print("error")
  else:
    result = list(q)
    if is_reverse:
      result.reverse()
    result = list(map(str,result))
    if len(result) == 0:
      print('[]')
    else:
      print("[" + ",".join(result) + "]")
