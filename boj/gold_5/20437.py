from collections import defaultdict

T = int(input())


def solution(input_text, cnt):
  number_dict = defaultdict(list)
  min_length = 99999999
  max_length = -1
  for i in range(len(input_text)):
    number_dict[input_text[i]].append(i)

  for key in number_dict:
    target_list = number_dict[key]
    this_min_length = 99999999
    this_max_length = -1
    for i in range(0, len(target_list) - cnt + 1):
      answer_length = target_list[i + cnt - 1] - target_list[i] + 1
      this_min_length = min(this_min_length, answer_length)
      this_max_length = max(this_max_length, answer_length)

    if this_max_length != -1:
      min_length = min(min_length, this_min_length)
      max_length = max(max_length, this_max_length)
  if max_length == -1:
    print(-1)
  else:
    print(min_length, max_length)
  return


for t in range(T):
  string = input()
  cnt = int(input())
  solution(string, cnt)
