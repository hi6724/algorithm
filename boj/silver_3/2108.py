from collections import Counter
import sys

input = sys.stdin.readline

answer = []
n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort()
#1
answer.append(round(sum(arr) / n))

#2
answer.append(arr[int(len(arr) / 2)])

#3
cnt = Counter(arr).most_common()
if len(cnt) == 1: answer.append(cnt[0][0])
else:
    if cnt[0][1] == cnt[1][1]: answer.append(cnt[1][0])
    else: answer.append(cnt[0][0])

#4
answer.append(arr[-1] - arr[0])

print(*answer, sep='\n')