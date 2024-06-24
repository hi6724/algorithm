n, m = map(int, input().split())
initN = n
binNum = bin(n)[2:]
cnt = binNum.count('1')
temp = 1
while cnt > m:
    n += n % 2**temp
    temp += 1
    binNum = bin(n)[2:]
    cnt = binNum.count('1')
print(n-initN)

