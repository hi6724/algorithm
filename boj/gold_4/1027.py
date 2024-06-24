import math

input()
buildings = list(map(int, input().split(' ')))
ans = 0

for i in range(len(buildings)):
    left_arr = []
    right_arr = []
    for j in range(i):
        temp = (buildings[j] - buildings[i]) / abs(i - j)
        left_arr.append(temp)
    for j in range(i + 1, len(buildings)):
        temp = (buildings[j] - buildings[i]) / abs(i - j)
        right_arr.append(temp)

    left_max = None
    left_cnt = 0
    for j in range(len(left_arr) - 1, -1, -1):
        if left_max == None:
            left_cnt += 1
            left_max = left_arr[j]
        elif left_max < left_arr[j]:
            left_cnt += 1
            left_max = left_arr[j]

    right_max = None
    right_cnt = 0
    for j in range(len(right_arr)):
        if right_max == None:
            right_cnt += 1
            right_max = right_arr[j]
        elif right_max < right_arr[j]:
            right_cnt += 1
            right_max = right_arr[j]
    ans = max(ans, right_cnt + left_cnt)
print(ans)