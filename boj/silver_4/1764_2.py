import sys

input = sys.stdin.readline

n, m = list(map(int, input().split(' ')))
first_list = {}
second_list = []
ans = []
for i in range(n):
    index = input().rstrip()
    first_list[index] = 1
for i in range(m):
    target = input().rstrip()
    if target in first_list:
        ans.append(target)
print(len(ans))
ans.sort()
for i in ans:
    print(i)