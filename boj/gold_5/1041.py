N = int(input())
numbers = list(map(int, input().split()))
s_2_list = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4],
]
s_3_list = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 4],
    [0, 3, 4],
    [5, 1, 2],
    [5, 1, 3],
    [5, 2, 4],
    [5, 3, 4],
]
s_2_count = sum(numbers)
s_3_count = sum(numbers)

for s in s_2_list:
    temp = numbers[s[0]] + numbers[s[1]]
    if temp < s_2_count:
        s_2_count = temp
for s in s_3_list:
    temp = numbers[s[0]] + numbers[s[1]] + numbers[s[2]]
    if temp < s_3_count:
        s_3_count = temp
s_2 = 4 + ((N - 2) * 8)
s_3 = 4
total_sides = (N**2) * 5
repeat = total_sides - (s_2 * 2 + s_3 * 3)
ans = 0
ans += s_2 * s_2_count
ans += s_3 * s_3_count
ans += repeat * min(numbers)
if N == 1:
    ans = sum(numbers)
    ans -= max(numbers)
print(ans)