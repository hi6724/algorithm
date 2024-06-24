import copy

n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
colors1 = ["R", "G", "B"]
colors2 = ["B", "G"]

for i in range(n):
    graph.append(list(input()))
temp = copy.deepcopy(graph)
count = 0
for color in colors1:
    for i in range(n):
        for j in range(n):
            q = []
            if temp[i][j] == color:
                q = [(i, j)]
                count += 1
            while q:
                x, y = q.pop()
                temp[x][y] = "X"
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if temp[nx][ny] == color:
                            q.append((nx, ny))

print(count, end=' ')

temp = copy.deepcopy(graph)
count = 0
for color in colors2:
    for i in range(n):
        for j in range(n):
            q = []
            if temp[i][j] != color and temp[i][j] != "X":
                q = [(i, j)]
                count += 1
            while q:
                x, y = q.pop()
                temp[x][y] = "X"
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if temp[nx][ny] != color and temp[nx][ny] != "X":
                            q.append((nx, ny))

print(count, end=' ')