import sys

input = sys.stdin.readline

test_case = int(input())
for i in range(test_case):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: (x[0], x[1]))
    x, y = arr[0][0], arr[0][1]
    count = 1
    for i in range(1, len(arr)):
        if arr[i][0] >= x and arr[i][1] <= y:
            count += 1
            x = arr[i][0]
            y = arr[i][1]
        elif arr[i][1] >= y and arr[i][0] <= x:
            count += 1
            x = arr[i][0]
            y = arr[i][1]

    print((count))