from collections import defaultdict, deque


def find(parent, x):
  if x == parent[x][0]:
    return x
  else:
    parent[x][0] = find(parent, parent[x][0])
    return parent[x][0]


def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)

  if parent[x][1] > parent[y][1]:
    parent[x][1] += parent[y][1]
    parent[y] = parent[x]
  else:
    if parent[x][0] == parent[y][0]:
      return
    else:
      parent[y][1] += parent[x][1]
      parent[x] = parent[y]


tc = int(input())
for _ in range(tc):
  ans = []
  N = int(input())
  graph = defaultdict(list)
  parent = defaultdict(lambda: "")

  for i in range(N):
    income = list(input().split(' '))
    income.sort()
    a, b = income
    if parent[a] == '':
      parent[a] = [a, 1]
    if parent[b] == '':
      parent[b] = [b, 1]
    union(parent, a, b)

    ans.append(parent[find(parent, a)][1])

  for row in ans:
    print(row)
