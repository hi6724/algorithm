def find(parent, x):
  if parent[x] == x:
    return x
  else:
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x


N = int(input())
M = int(input())
parent = [0]

for cur_node in range(1,N+1):
  parent.append(cur_node)

for cur_node in range(1,N+1):
  income = list(map(int, input().split(" ")))
  for node,check in enumerate(income):
    if check==1:
      union(parent,node+1,cur_node)

plan = list(map(int,input().split(' ')))

prev = parent[plan[0]]
ans="YES"
for p in plan:
  if prev !=parent[p]:
    ans = "NO"
    break
print(ans)
  