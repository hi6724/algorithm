N, M = map(int, input().split(' '))
ropes = []
for i in range(N):
    ropes.append(int(input()))

right = max(ropes)
left = 1

while left <= right:
    mid = (right+left)//2
    cnt = 0
    for rope in ropes:
        cnt += rope//mid
    if cnt >= M:
        left = mid + 1
    else:
        right = mid - 1


print(right)
