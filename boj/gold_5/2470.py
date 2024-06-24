from math import inf


input()
arr = list(map(int, input().split(" ")))

q_left = []
q_right = []
for tempValue in arr:
    if tempValue < 0:
        q_left.append(tempValue)
    else:
        q_right.append(tempValue)
q_left.sort(reverse=True)
q_right.sort()

ans = [inf, -1, -1]

if len(q_right) > 1:
    ans = [abs(q_right[0]+q_right[1]), q_right[0], q_right[1]]
if len(q_left) > 1:
    if abs(q_left[1]+q_left[0]) < ans[0]:
        ans = [abs(q_left[1]+q_left[0]), q_left[1], q_left[0]]


if len(q_left) == 0:
    print(q_right[0], q_right[1])
elif len(q_right) == 0:
    print(q_left[1], q_left[0])

else:
    left = q_left.pop()
    right = q_right.pop()

    while True:
        if(abs(left+right) < ans[0]):
            ans = [abs(left+right), left, right]
        if(left+right >= 0):
            if q_right:
                right = q_right.pop()
            else:
                break
        else:
            if q_left:
                left = q_left.pop()
            else:
                break
    print(ans[1], ans[2])
