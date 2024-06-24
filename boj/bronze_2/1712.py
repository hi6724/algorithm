A, B, C = map(int, input().split(" "))
if C - B <= 0:
    print(-1)
else:
    print(int(A / (C - B) + 1))
