n = input()
arr = []
for i in range(int(n)):
    x, y = map(int, input().split(' '))
    arr.append((x, y))
arr = sorted(arr)
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
