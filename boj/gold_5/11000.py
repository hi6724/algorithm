# https://www.acmicpc.net/problem/11000
import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])
ans_list = []
heapq.heappush(ans_list, 0)

for i in arr:
    node = heapq.heappop(ans_list)
    if node <= i[0]:
        pass
    else:
        heapq.heappush(ans_list, node)
    heapq.heappush(ans_list, i[1])
print(len(ans_list))
