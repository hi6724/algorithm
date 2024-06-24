first = input()
second = input()

n = len(first)
m = len(second)
temp = ''
for i in range(m):
    temp += '0'
first = temp + first + temp
repeat = len(first) - len(second)
ans = 1000
for i in range(repeat + 1):
    temp1 = ''
    temp2 = ''
    for j in range(i):
        temp1 += '0'
    for j in range(repeat - i):
        temp2 += '0'
    temp_second = temp1 + second + temp2
    temp_ans = ''
    for i in range(len(first)):
        temp_ans += str(int(first[i]) + int(temp_second[i]))
    temp_ans = temp_ans.strip('0')
    ok = True
    for t in temp_ans:
        if int(t) > 3:
            ok = False
    if ok:
        if ans > len(temp_ans):
            ans = len(temp_ans)
print(ans)