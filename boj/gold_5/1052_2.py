ans = 0
n, m = list(map(int, input().split()))
temp = bin(n)[2:]
count = temp.count('1')
while count > m:
    n += 1
    ans += 1
    temp = bin(n)[2:]
    count = temp.count('1')
print(ans)