n = int(input())
arr = []
ans_arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    ans_arr.append(arr[i] * (n - i))
print(max(ans_arr))