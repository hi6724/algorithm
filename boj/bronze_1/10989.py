import sys

n = int(sys.stdin.readline())
dic = {}
for i in range(int(n)):
    x = int(sys.stdin.readline())
    try:
        dic[x] += 1
    except:
        dic[x] = 1

for i in range(int(max(dic)) + 1):
    try:
        for j in range(dic[i]):
            print(i)
    except:
        pass