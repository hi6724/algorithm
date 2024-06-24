n = input()
data_list = list(map(int, input().split()))
data_list.sort()
ans = 0
for i in range(len(data_list)):
    ans += (data_list[i] * (len(data_list) - i))

print(ans)