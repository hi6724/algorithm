from itertools import permutations
N = int(input())

scores = []
for i in range(N):
  score_list = list(map(int, input().split(' ')))
  scores.append(score_list)

ans = 0
for idx_arr in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
  idx_arr = list(idx_arr)
  idx_arr = idx_arr[:3]+[0]+idx_arr[3:]
  total = 0
  # idx_arr = 타석에 서는 순서
  index = 0

  for i in range(N):
    out_cnt = 0
    first = 0
    second = 0
    third = 0

    cur_score_arr = scores[i]
    temp = []

    while out_cnt <= 2:
      hit = cur_score_arr[idx_arr[index]]

      if hit == 0:
        out_cnt += 1
      elif hit == 1:
        if third == 1:
          total += 1
          third = 0
        if second == 1:
          third = 1
          second = 0
        if first == 1:
          second = 1
          first = 0
        first = 1
      elif hit == 2:
        if third == 1:
          total += 1
          third = 0
        if second == 1:
          total += 1
          second = 0
        if first == 1:
          third = 1
          first = 0
        second = 1
      elif hit == 3:
        if third == 1:
          total += 1
          third = 0
        if second == 1:
          total += 1
          second = 0
        if first == 1:
          total += 1
          first = 0
        third = 1
      elif hit == 4:
        if third == 1:
          total += 1
          third = 0
        if second == 1:
          total += 1
          second = 0
        if first == 1:
          total += 1
          first = 0
        total += 1
      index += 1
      index %= 9
      # print(temp)
  if total > ans:
    ans = total
print(ans)
