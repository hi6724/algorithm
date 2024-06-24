n = int(input())

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
for i in range(10):
    t = []
    for j in range(i):
        arr.append(str(i) + str(j))
        t.append(str(i) + str(j))
    temp.append(t)
for i in range(4):
    temp_2 = [[]]
    for i in range(1, 10):
        t = []
        for j in range(1, i):
            for add_str in temp[j]:
                tt = str(i)
                tt += add_str
                t.append(tt)
                arr.append(tt)
        temp_2.append(t)

    temp = [[]]
    for i in range(1, 10):
        t = []
        for j in range(1, i):
            for add_str in temp_2[j]:
                tt = str(i)
                tt += add_str
                t.append(tt)
                arr.append(tt)
        temp.append(t)
try:
    print(arr[n])
except:
    print(-1)