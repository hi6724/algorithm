loop = int(input())

for i in range(loop):
    temp = ''
    for j in range(loop):
        if i >= j:
            temp += '*'
    for j in range(loop-len(temp)):
        temp += ' '
    for j in range(len(temp)):
        print(temp[loop-j-1], end='')
    print()
