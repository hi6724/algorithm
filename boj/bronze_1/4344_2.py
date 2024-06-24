num = int(input())
for i in range(num):
    students = input().split(" ")
    total = int(students[0])
    del students[0]
    for i in range(len(students)):
        students[i] = int(students[i])
    average = sum(students) / total
    count = 0
    for student in students:
        if student > average:
            count += 1
    print(round((count / total) * 100, 3), end="")
    print("%")
