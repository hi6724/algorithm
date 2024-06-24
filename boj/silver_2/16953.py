# 백준 16953
a, b = input().split()
count = 1
while int(b) > int(a):
    if b[-1] == "1":
        b = b[:-1]
        count += 1
    elif int(b) % 2 == 0:
        temp = int(int(b) / 2)
        b = str(temp)
        count += 1
    else:
        count = -1
        break
if a == b:
    print(count)
else:
    print(-1)