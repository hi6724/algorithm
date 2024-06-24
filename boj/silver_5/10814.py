n = input()
arr = []
for i in range(int(n)):
    x, y = input().split(' ')
    arr.append((int(x), y))
arr = sorted(arr, key=lambda x: x[0])
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
