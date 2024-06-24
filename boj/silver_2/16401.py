p, i = map(int, input().split(' '))
cookies = list(map(int, input().split(' ')))

left = 1
right = max(cookies)
mid = (left+right)//2

while True:
    cnt = 0
    for cookie in cookies:
        cnt += cookie//mid
    if right == left or left+1 == right:
        break
    if cnt >= p:
        left = mid
    else:
        right = mid-1
    mid = (left+right)//2

ans = 0
cnt = 0
for cookie in cookies:
    cnt += cookie//left
if cnt >= p:
    ans = left

cnt = 0
for cookie in cookies:
    cnt += cookie//right
if cnt >= p:
    ans = right


print(ans)
