loop = int(input())

for i in range(loop):
    for j in range(loop):
        if i >= j:
            print("*", end='')
    print()
