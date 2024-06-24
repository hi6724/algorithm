import sys
while(True):
    try:
        x = int(sys.stdin.readline()) * 10000000
        n = int(sys.stdin.readline())

        if(n == 0):
            print('danger')
            continue
        elif(n == 1):
            sys.stdin.readline()
            print('danger')
            continue
        li = []
        for i in range(n):
            li.append(int(sys.stdin.readline()))
        li.sort()
        start = 0
        end = n-1
        while (True):
            if(li[start] + li[end] == x):
                print('yes', li[start], li[end])
                break
            elif(li[start] + li[end] > x):
                end -= 1
            elif (li[start] + li[end] < x):
                start += 1
            if(start >= end):
                print('danger')
                break
    except:
        break
