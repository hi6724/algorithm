temp = input()
temp = temp.split(" ")
result = int(temp[0]) - int(temp[1])

if result < 0:
    print("<")
elif result > 0:
    print(">")
else:
    print("==")
