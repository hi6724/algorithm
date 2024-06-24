n, m = list(map(int, input().split()))
brands = []
for i in range(m):
    brands.append(list(map(int, input().split())))
temp = []
set_brands = sorted(brands, key=lambda x: x[0])[0]
ind_brands = sorted(brands, key=lambda x: x[1])[0]
ans = 0
if ind_brands[1] * 6 < set_brands[0]:
    ans += n * ind_brands[1]
elif (n % 6) * ind_brands[1] > set_brands[0]:
    ans += (n // 6) * set_brands[0]
    ans += set_brands[0]
else:
    ans += (n // 6) * set_brands[0]
    ans += (n % 6) * ind_brands[1]
print(ans)