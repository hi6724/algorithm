# https://www.acmicpc.net/problem/1080

n, m = list(map(int, input().split()))
mat_a = []
mat_b = []

for i in range(n):
    mat_a.append(list(input()))
for i in range(n):
    mat_b.append(list(input()))
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if mat_b[i][j] != mat_a[i][j]:
            try:
                for x in range(3):
                    for y in range(3):
                        if mat_b[i + x][j + y] == '0':
                            mat_b[i + x][j + y] = '1'
                        else:
                            mat_b[i + x][j + y] = '0'
                ans += 1
            except:
                pass
if mat_a == mat_b:
    print(ans)
else:
    print(-1)
