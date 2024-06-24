target = int(input().split(" ")[1])
arr = list(map(int, input().split(' ')))

arr.sort()
print(arr[target-1])