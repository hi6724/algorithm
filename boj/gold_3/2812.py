# https://www.acmicpc.net/problem/2812
n, m = list(map(int, input().split()))
target = list(map(int, input()))
ans = []
index = 0
count = 0
for t in target:
    while count < m:
        try:
            if ans[-1] < t:
                ans.pop()
                count += 1
            else:
                break
        except:
            break
    ans.append(t)
if count != m:
    for i in range(m - count):
        ans.pop()
for i in ans:
    print(i, end='')
