n, s, m = map(int, input().split())

volume = list(map(int, input().split()))
temp = set()
is_ok = True
if s - volume[0] >= 0:
    temp.add(s - volume[0])
if s + volume[0] <= m:
    temp.add(s + volume[0])
volume[0] = temp
for i in range(1, len(volume)):
    temp = set()
    if len(volume[i - 1]) < 1:
        print(-1)
        is_ok = False
        break
    for j in volume[i - 1]:
        if j + volume[i] <= m:
            temp.add(j + volume[i])
        if j - volume[i] >= 0:
            temp.add(j - volume[i])
    volume[i] = temp

if is_ok:
    if len(volume[-1]) < 1:
        print(-1)
    else:
        print(max(volume[-1]))