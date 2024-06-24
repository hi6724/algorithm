target = int(input())
M = int(input())
num_list = []
if M != 0:
    num_list = list(map(int, input().split(' ')))

cur_num = 100
min_range = 999999
min_pos = -1
# 채널 N에 가장 근접한 번호로 이동하기
for i in range(0, 1000001):
    is_ok = True
    for num in num_list:
        if str(num) in str(i):
            is_ok = False
    if is_ok:
        if min_range > abs(i - target):
            min_range = abs(i - target)
            min_pos = i

ans = len(str(min_pos)) + abs(min_pos - target)
if min_pos == -1:
    ans = 999999
if abs(target - 100) < ans:
    ans = abs(target - 100)
print(ans)
