n = input()
if n=="9":
    print(11)
elif len(n) % 2 == 0:
    cnt = int(len(n) // 2)
    front = (n[:cnt])
    back = ''
    for i in range(cnt):
        back += front[-1 - i]
    total = front + back
    while int(total) <= int(n):
        front = str(int(front) + 1)
        back = ''
        for i in range(cnt):
            back += front[-1 - i]
        total = front + back
    if len(front) > cnt:
        total = int(total) + 1
    print(total)
else:
    cnt = int(len(n) // 2)
    front = (n[:cnt])
    center = n[cnt]
    back = ''
    for i in range(cnt):
        back += front[-1 - i]
    total = front + center + back
    while int(total) <= int(n):
        center = str(int(center) + 1)
        if int(center) > 9:
            center = '0'
            front = str(int(front) + 1)
            back = ''
            for i in range(cnt):
                back += front[-1 - i]
        total = front + center + back
    if len(front) > cnt:
        total = int(total) + 1
    print(total)
