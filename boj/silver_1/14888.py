# 수가 11개, 연산자가 10개
# [1,2,3,4,1,2,3,4,1,2]
# [1,1,1,2,2,2,3,3,4,4]
# [1,1,1],[2,2,2],[3,3][4,4]
# 10C3 7C3 4C2
from itertools import combinations
from math import inf

N = int(input())
nums = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))
operators_comb = []
max_value = -inf
min_value = inf

# 더하기 들어갈 곳
plus_comb = combinations(range(N-1), operators[0])
for plus in plus_comb:
  filtered_list1 = [item for item in list(range(N-1)) if item not in plus]
  minus_comb = combinations(filtered_list1, operators[1])
  for minus in minus_comb:
    filtered_list2 = [item for item in filtered_list1 if item not in minus]
    multiple_comb = combinations(filtered_list2, operators[2])
    for multiple in multiple_comb:
      divide = [item for item in filtered_list2 if item not in multiple]
      temp_operators = [-1 for _ in range(N-1)]
      for plus_index in plus:
        temp_operators[plus_index] = '+'
      for minus_index in minus:
        temp_operators[minus_index] = '-'
      for multiple_index in multiple:
        temp_operators[multiple_index] = '*'
      for divide_index in divide:
        temp_operators[divide_index] = '/'
      result = nums[0]
      for oper_index, oper in enumerate(temp_operators):
        next_num = nums[oper_index+1]
        if oper == '+':
          result = result + next_num
        elif oper == '-':
          result = result - next_num
        elif oper == '*':
          result = result * next_num
        elif oper == '/':
          result = int(result / next_num)

      max_value = max(max_value, result)
      min_value = min(min_value, result)
print(max_value)
print(min_value)
