
def sol(n):
    result = 0
    for i in n:
        result += int(i)
    result += int(n)
    try:
        ans[result] = 0
    except:
        pass
    return result


ans = []
for i in range(10001):
    ans.append(1)

for i in range(10001):
    (sol(str(i)))
for i in range(10001):
    if ans[i] == 1:
        print(i)
