# N , M <= 50

n, m = map(int, input().split())
arr = list(map(int, input().split(" ")))
ans = 0


arr.sort()

pArr = []
nArr = []
for el in arr:
    if el > 0:
        pArr.append(el)
    else:
        nArr.append(abs(el))
nArr.sort()
nMax = 0
pMax = 0
if len(nArr) > 0:
    nMax = nArr[-1]

if len(pArr) > 0:
    pMax = pArr[-1]

if nMax > pMax:
    ans -= nMax
else:
    ans -= pMax

while nArr:
    for i in range(m):
        try:
            if i == 0:
                cnt = nArr.pop()
            else:
                nArr.pop()
        except:
            pass
    ans += cnt*2

while pArr:
    for i in range(m):
        try:
            if i == 0:
                cnt = pArr.pop()
            else:
                pArr.pop()
        except:
            pass
    ans += cnt*2

print(ans)
