n = input()
roads = list(map(int, input().split(' ')))
cities = list(map(int, input().split(' ')))
ans = 0
temp = [0]
min_city = 0
for i in range(len(cities) - 1):
    if cities[temp[-1]] > cities[i + 1]:
        temp.append(i + 1)
temp.append(len(cities) - 1)

for i in range(len(temp) - 1):
    len_road = 0
    for j in range(temp[i], temp[i + 1]):
        # print(j)
        len_road += roads[j]
    # print(len_road)
    # print(cities[temp[i]])
    # print()
    ans += cities[temp[i]] * len_road
print(ans)