import sys

input = lambda: sys.stdin.readline().strip()
n = int(input())
m = [0] * 1000001
m[1] = 1
m[2] = 2
for i in range(3, n + 1):
    m[i] = (m[i - 2] + m[i - 1]) % 15746
print(m[n])