while True:
    check = input()

    if check == '0':
        break
    is_true = True
    for i in range(len(check)//2):
        if check[i] != check[-1-i]:
            is_true = False
    if is_true:
        print("yes")
    else:
        print('no')
