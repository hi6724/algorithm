N=int(input())
arr=list(map(int,input().split(" ")))
ansList=[1 for _ in range(N)]

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i]>arr[j]:
            ansList[i]=max(ansList[i],ansList[j]+1)
print(max(ansList))
