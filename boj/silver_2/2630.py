'''
input
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
result 
9
7
'''


def divide(arr):
  total = 0
  global white_cnt, blue_cnt
  for i in arr:
    total += sum(i)
  if total == 0:
    white_cnt += 1
    return arr
  if total == len(arr)**2:
    blue_cnt += 1
    return arr

  for i in range(4):
    x = i//2
    y = i % 2
    new_arr = []
    for dx in range(len(arr)//2):
      temp = []
      for dy in range(len(arr)//2):
        nx = x*len(arr)//2 + dx
        ny = y*len(arr)//2 + dy
        temp.append(arr[nx][ny])
      new_arr.append(temp)
    new_arr = divide(new_arr)


N = int(input())
board = []
white_cnt = 0
blue_cnt = 0
for i in range(N):
  row = list(map(int, input().split(' ')))
  board.append(row)

result = divide(board)
print(white_cnt)
print(blue_cnt)
