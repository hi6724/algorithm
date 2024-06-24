n = int(input())
kit_list = list(map(int, input().split(' ')))
average = sum(kit_list) / len(kit_list)
kit_list = list(map(lambda x: int(x - average), kit_list))
ans = 0

for i in range(len(kit_list)):
    judge = 1
    if kit_list[i] < 0:
        judge = -1

    while kit_list[i] * judge > 0:
        for j in range(i + 1, len(kit_list)):
            if kit_list[j] != 0:
                kit_list[j] += judge
                kit_list[i] -= judge
                ans += (j - i)
                break
print(ans)
