input()
arr = list(map(int, input().split(' ')))

left = [[arr[0], 1]]
ans = [0]
for i in range(1, len(arr)):
    while True:
        try:
            if arr[i] > left[-1][0]:
                left.pop()
            else:
                break
        except:
            break
    if len(left) == 0:
        ans.append(0)
    else:
        ans.append(left[-1][-1])
    left.append([arr[i], i + 1])
for i in ans:
    print(i, end=' ')
