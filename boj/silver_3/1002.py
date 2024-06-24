def sol(x1, y1, r1, x2, y2, r2):
    distance = (((x2 - x1)**2 + (y2 - y1)**2))**(1 / 2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    else:
        print(0)


n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    sol(x1, y1, r1, x2, y2, r2)
