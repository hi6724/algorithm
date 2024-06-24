n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))
ans_arr = []
now_time = 0
for i in arr:
    if i[0] >= now_time:
        ans_arr.append(i)
        now_time = i[1]

print(len(ans_arr))