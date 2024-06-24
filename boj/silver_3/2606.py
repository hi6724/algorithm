cnt=int(input())
n= int(input())
arr=[]
for i in range(cnt+1):
    arr.append([])
for i in range(n):
    x , y=map(int,input().split(" "))
    arr[x].append(y)
    arr[y].append(x)

q=[1]
visited=[1]

while q:
    node=q.pop()
    nodes=arr[node]
    for x in nodes:
        if x not in visited:
            q.append(x)
            visited.append(x)
print(len(visited)-1)     
                 