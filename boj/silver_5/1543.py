def sol(root, target):
    ans = []
    i = 0
    while i < (len(root) - len(target) + 1):
        temp = ''
        temp_index = []

        for j in range(len(target)):
            temp += root[i + j]
            temp_index.append(i + j)
        if temp == target:
            ans.append(temp_index)
            i += len(target)
        else:
            i += 1
    print(len(ans))


chars = input()
target = input()
sol(chars, target)