import sys


def sol(test):
    ans = [test[0]]
    for i in test:
        if ans[-1] == i:
            pass
        elif i not in ans:
            ans.append(i)
        else:
            return 0
    return 1


n = int(sys.stdin.readline())
count = 0
for i in range(n):
    count += sol(sys.stdin.readline())
print(count)