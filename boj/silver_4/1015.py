def sol(N, arr):
    result = []
    ans = ''
    for i in range(len(arr)):
        count = 0
        count_arr = arr[:i]
        for c in count_arr:
            if c <= arr[i]: count += 1
        for j in arr[i + 1:]:
            if arr[i] > j:
                count += 1
        print(count, end=" ")


n = int(input())
arr = list(map(int, input().split()))
sol(n, arr)
