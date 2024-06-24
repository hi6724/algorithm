n = list(map(int, list(input())))
if 0 not in n:
    print(-1)
else:
    temp = 0
    for i in range(len(n)):
        temp += int(n[i])
    if temp % 3 == 0:
        n.sort(reverse=True)
        for i in n:
            print(i, end='')
    else:
        print(-1)
