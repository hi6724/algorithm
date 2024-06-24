import sys

input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    s, e = map(int, input().split(' '))
    arr.append((s, e))
arr.sort()

ans = 0
prev_s = arr[0][0]
prev_e = arr[0][1]
arr.pop(0)

for s, e in arr:
    if s <= prev_e:
        if e > prev_e:
            prev_e = e

    if s > prev_e:
        ans += (prev_e - prev_s)
        prev_s = s
        prev_e = e
ans += (prev_e - prev_s)
print(ans)