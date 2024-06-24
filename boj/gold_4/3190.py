# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

l = int(input())
dir_dict = dict()
q = deque()
q.append((0, 0))

for i in range(l):
    x, d = input().split()
    dir_dict[int(x)] = d
x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0


def turn(n):
    global direction
    if n == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))
        if cnt in dir_dict:
            turn(dir_dict[cnt])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        graph[tx][ty] = 0
        if cnt in dir_dict:
            turn(dir_dict[cnt])
    else:
        break
print(cnt)