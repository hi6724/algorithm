from collections import deque
TC=int(input())

for i in range(TC):
    arr=[]
    dp=deque()
    dp.append([0,0])
    dp.append([0,0])
    N=int(input())
    arr.append(list(map(int,input().split(" "))))
    arr.append(list(map(int,input().split(" "))))
    arr[0].append(0)
    arr[0].append(0)
    arr[1].append(0)
    arr[1].append(0)

    for j in range(N-1,-1,-1):
        tempList=[0,0]
        
        
        tempList[0]=arr[0][j]
        tempList[0]+=max(dp[0][1],dp[1][1])

        tempList[1]=arr[1][j]
        tempList[1]+=max(dp[0][0],dp[1][0])

        dp.appendleft(tempList)
        dp.pop()
    print(max(dp[0]))