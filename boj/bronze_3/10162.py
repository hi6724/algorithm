n = int(input())
timers = [300, 60, 10]
ans_arr = []
for time in timers:
    temp = 0
    if n >= time:
        temp = n // time
        n -= (n // time) * time
    ans_arr.append(temp)
if sum(ans_arr) == 0:
    print(-1)
elif n != 0:
    print(-1)
else:
    for i in ans_arr:
        print(i, end=" ")
