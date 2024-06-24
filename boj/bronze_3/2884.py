temp = input()
temp = temp.split(" ")
H = int(temp[0])
M = int(temp[1])
if M >= 45:
    print(H, M - 45)
elif H == 0:
    print(23, M + 15)
else:
    print(H - 1, M + 15)