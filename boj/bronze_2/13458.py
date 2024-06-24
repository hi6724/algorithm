from math import ceil

N = int(input())
class_room_list = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))

class_room_list = list(map(lambda x: x-B, class_room_list))
cnt = N
for class_room in class_room_list:
  if class_room > 0:
    cnt += ceil(class_room/C)
print(cnt)
