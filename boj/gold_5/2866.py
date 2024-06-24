R, C = map(int, input().split(' '))
strs = ["" for _ in range(C)]
for i in range(R):
    income = list(input())
    for j in range(len(income)):
        strs[j] += income[j]
ans = 0
for l in range(1, len(strs[0])):
    temp = set()
    for i in range(C):
        temp.add(strs[i][l:])
    if len(temp) == C:
        ans += 1
    else:
        break
print(ans)
