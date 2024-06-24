n = int(input())

root_arr = []
ans = {}
for i in range(n):
    item = input()
    if item in ans:
        ans[item] += 1
    else:
        ans[item] = 1
ans_list = list(ans.items())
ans_list.sort()
max_value = (max(ans_list, key=lambda x: x[1]))
print(max_value[0])
