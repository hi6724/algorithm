# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))

ans = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans))
