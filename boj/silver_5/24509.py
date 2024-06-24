import sys

arrs2 = [[], [], [], []]
n = int(sys.stdin.readline())
for _ in range(n):
    i, a, b, c, d = map(int, sys.stdin.readline().split())
    arrs2[0].append((i, a))
    arrs2[1].append((i, b))
    arrs2[2].append((i, c))
    arrs2[3].append((i, d))

ans = []
for arr in arrs2:
    ss = sorted(arr, reverse=True, key=lambda sort_key: (sort_key[1], -sort_key[0]))

    for i in range(len(ss)):
        if ss[i][0] not in ans:
            ans.append(ss[i][0])
            break
for i in ans:
    print(i, end=" ")