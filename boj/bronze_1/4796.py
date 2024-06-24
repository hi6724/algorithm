index = 0
while True:
    index += 1
    L, P, V = list(map(int, input().split()))
    ans = 0
    if L + P + V == 0:
        break
    a = V // P
    b = V % P
    if L < b:
        b = L
    ans = a * L + b
    print(f"Case {index}:", ans)
