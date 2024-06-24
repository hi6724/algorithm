from collections import deque

gear_1 = deque(list(map(int,list(input()))))
gear_2 = deque(list(map(int,list(input()))))
gear_3 = deque(list(map(int,list(input()))))
gear_4 = deque(list(map(int,list(input()))))
N = int(input())
gear_list = [gear_1,gear_2,gear_3,gear_4]

def get_score():
  global gear_list
  score = 0
  for i in range(4):
    cur_gear = gear_list[i]
    score+=cur_gear[0]*(2**i)
  return score

def turn(arr,direction):
  if direction==1:
    item = arr.pop()
    arr.appendleft(item)
  else:
    item = arr.popleft()
    arr.append(item)

# 위 0
# 오른 2
# 밑 4
# 왼 6
# 1이면 시계 -1 반시계

for _ in range(N):
  j,direction = map(int,input().split(' '))
  init = j -1

  targets=[init]
  for j in range(1,4 - init):
    next_gear = gear_list[init+j]
    if next_gear[6] != gear_list[init+j-1][2]:
      targets.append(init+j)
    else:
      break

  # print("PREV:::")
  for prev_index in range(init-1,-1,-1):

    if gear_list[prev_index][2] != gear_list[prev_index+1][6]:
      # print("OKOK::",prev_index,prev_index+1)
      # print(gear_list[prev_index])
      # print(gear_list[prev_index+1])
      targets.append(prev_index)
    else:
      break


  for target_index in targets:
    target_gear = gear_list[target_index]
    judge = (target_index - init) % 2
    target_direction = direction
    if judge == 1:
      target_direction = -direction
    turn(target_gear,target_direction)



# 2개떨어져있으면 *1 1개  떨어져있으면 *-1
print(get_score())
