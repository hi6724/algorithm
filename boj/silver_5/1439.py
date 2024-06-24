n = input()
one_arr = (n.split("1"))
zero_arr = (n.split("0"))
ans_0 = 0
ans_1 = 0

for i in zero_arr:
    if len(i) > 0:
        ans_0 += 1
for i in one_arr:
    if len(i) > 0:
        ans_1 += 1

print(min(ans_0, ans_1))
