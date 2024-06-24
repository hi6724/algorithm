n = int(input())
arr = list(map(int, input().split()))   # 수열 A: idx 0 ~ n-1

dp = [1]*len(arr)

def solution_dp():
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

solution_dp()