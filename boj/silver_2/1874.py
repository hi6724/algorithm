n = int(input())

target = []
for i in range(n):
    target.append(int(input()))

stack = [1]
ans = ['+']
cnt = 2
index = 0

while index < n and cnt <= n+1:

    target_num = target[index]
    if len(stack) == 0:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if target_num == stack[-1]:
        stack.pop()
        ans.append('-')
        index += 1
    else:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
if cnt > n+1:
    print("NO")
else:
    for a in ans:
        print(a)
