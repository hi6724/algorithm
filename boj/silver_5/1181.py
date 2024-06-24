total_length = int(input())
temp = set()
for i in range(total_length):
    temp.add(input())

incomes = list(temp)
incomes.sort(key=lambda x: [len(x), x])
for el in incomes:
    print(el)
