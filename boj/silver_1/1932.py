n = int(input())
v = []
for i in range(n):
    v.append(list(map(int, input().split())))
if n == 1:
    print(v[0][0])
else:
    v[1] = [v[0][0] + v[1][0], v[0][0] + v[1][1]]
    for i in range(2, n):
        for j in range(1, len(v[i]) - 1):
            v[i][j] = max(v[i - 1][j - 1], v[i - 1][j]) + v[i][j]
        v[i][0] = v[i][0] + v[i - 1][0]
        v[i][-1] = v[i][-1] + v[i - 1][-1]
    print(max(v[-1]))