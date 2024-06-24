n = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
a_arr.sort()
b_arr.sort(reverse=True)
ans = 0
for i in range(n):
    ans += a_arr[i] * b_arr[i]
print(ans)