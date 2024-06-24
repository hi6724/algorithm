n, c = list(map(int, input().split()))
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

max_gap = array[-1] - array[0]
min_gap = 1
result = 0
while max_gap >= min_gap:
    center_gap = (max_gap + min_gap) // 2
    count = 1
    value = array[0]
    for i in array:
        if i >= value + center_gap:
            value = i
            count += 1
    if count >= c:
        min_gap = center_gap + 1
        result = center_gap
    if count < c:
        max_gap = center_gap - 1
print(result)