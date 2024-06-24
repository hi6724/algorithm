def sol(x, y, test):
    pattern = [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
    ]
    count = []
    for x_index in range(x - 7):
        for y_index in range(y - 7):
            # check
            count_item = 0
            for i in range(x_index, 8 + x_index):
                for j in range(y_index, 8 + y_index):
                    if test[i][j] != pattern[i - x_index][j - y_index]:
                        count_item += 1
            count.append(count_item)
    print(min(64 - max(count), min(count)))


arr = []
x, y = map(int, input().split())
for i in range(x):
    arr.append(input())
count = sol(x, y, arr)
