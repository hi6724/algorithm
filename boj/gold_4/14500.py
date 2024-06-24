# https://www.acmicpc.net/problem/14500

patterns = []

# l
pattern1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
pattern2 = [[0, 0], [1, 0], [2, 0], [3, 0]]
# ㅁ
pattern3 = [[0, 0], [1, 0], [0, 1], [1, 1]]
# L
pattern4 = [[0, 0], [0, 1], [0, 2], [1, 0]]
pattern5 = [[0, 0], [0, 1], [0, 2], [-1, 0]]

pattern6 = [[0, 0], [1, 0], [2, 0], [2, 1]]
pattern7 = [[0, 0], [-1, 0], [-2, 0], [-2, 1]]

pattern8 = [[0, 0], [1, 0], [1, -1], [1, -2]]
pattern9 = [[0, 0], [-1, 0], [-1, -1], [-1, -2]]

pattern10 = [[0, 0], [0, 1], [1, 1], [2, 1]]
pattern11 = [[0, 0], [0, 1], [-1, 1], [-2, 1]]

# z
pattern12 = [[0, 0], [0, -1], [1, -1], [1, -2]]
pattern13 = [[0, 0], [0, -1], [-1, -1], [-1, -2]]

pattern14 = [[0, 0], [1, 0], [1, 1], [2, 1]]
pattern15 = [[0, 0], [-1, 0], [-1, 1], [-2, 1]]
# ㅗ
pattern16 = [[0, 0], [1, 0], [2, 0], [1, -1]]
pattern17 = [[0, 0], [1, 0], [2, 0], [1, 1]]
pattern18 = [[0, 0], [0, -1], [0, -2], [1, -1]]
pattern19 = [[0, 0], [0, -1], [0, -2], [-1, -1]]
patterns.extend([
    pattern1,
    pattern2,
    pattern3,
    pattern4,
    pattern5,
    pattern6,
    pattern7,
    pattern8,
    pattern9,
    pattern10,
    pattern11,
    pattern12,
    pattern13,
    pattern14,
    pattern15,
    pattern16,
    pattern17,
    pattern18,
    pattern19,
])
ans = 0
n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
for p in patterns:
    for i in range(n):
        for j in range(m):
            temp = 0
            for k in range(4):
                nx = i + p[k][0]
                ny = j + p[k][1]
                if 0 <= nx < n and 0 <= ny < m:
                    temp += (mat[i + p[k][0]][j + p[k][1]])
                else:
                    temp = -99
            if temp > ans:
                ans = temp
print(ans)