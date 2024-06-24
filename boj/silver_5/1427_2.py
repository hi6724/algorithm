n = input()
arr = []
result = ''
for i in n:
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    result += str(i)
print(result)