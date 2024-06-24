from math import log10,floor

tc = int(input())
for TC in range(tc):
    num = int(input())
    start = 0
    for i in range(num):
        start+=log10(i+1)
    print(floor(start)+1)