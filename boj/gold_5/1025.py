# https://www.acmicpc.net/problem/1025

import math
import itertools

n, m = map(int, input().split())
t = max(n, m)
test = []
for i in range(n):
    test.append(list(map(int, list(input()))))

index = '0123456789'
s_dict = {}
for s in index:
    s_dict[s] = []
max_num = math.floor((10**t)**0.5) + 1
# max 1000번 반복
for i in range(n):
    for j in range(m):
        t = str(test[i][j])
        s_dict[t].append([i, j])
ans = []
for kk in range(4):
    for t in test:
        if kk**2 in t:
            ans.append(kk**2)

for kk in range(4, max_num):
    string = str(kk**2)
    start = s_dict[string[0]]
    second = s_dict[string[1]]
    tt = list(itertools.product(start, second))
    for i in tt:
        dx, dy = (i[1][0] - i[0][0], i[1][1] - i[0][1])
        nx = i[1][0] + dx
        ny = i[1][1] + dy
        temp = string[0] + string[1]
        for s in range(2, len(string)):
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            try:
                if int(string[s]) != test[nx][ny]:
                    break
            except:
                break
            nx += dx
            ny += dy
            temp += string[s]
        if temp == string:
            ans.append(int(string))
            break
if len(ans) > 0:
    print(max(ans))
else:
    print(-1)
