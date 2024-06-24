import sys

input = sys.stdin.readline


def sol(arr):
    cache = [None] * len(arr)
    cache[0] = arr[0]

    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i - 1]) + arr[i]

    ans = []
    start = 0
    end = 0
    t_max = max(cache)
    if t_max <= 0:
        for i in range(len(cache)):
            if cache[i] == t_max:
                return (t_max, i + 1, i + 1)
                break
    else:
        for i in range(len(cache)):
            if cache[i] <= 0:
                start = i + 1
            if cache[i] == t_max:
                end = i
                ans.append([end - start, start, end])
        ans.sort()
        return (t_max, ans[0][1] + 1, ans[0][2] + 1)


arrs = []
ans = []
n = int(input())

for i in range(n):
    input()
    j = list(map(int, input().split(' ')))
    arrs.append(j)
for arr in arrs:
    ans.append(sol(arr))
total = 0
for a in ans:
    total += a[0]
print(total)
for a in ans:
    print(a[1], a[2])
