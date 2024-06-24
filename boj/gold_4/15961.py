# 밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
from collections import deque

n, d, k, c = map(int, input().split())
board = []
ansDict = {}
for i in range(n):
    temp = int(input())
    board.append(temp)
    ansDict[temp] = 0

ansDict[c] = n+1
maxValue = 0
ans = 0

window = deque()
for i in range(k):
    window.append(board[i])
    ansDict[board[i]] += 1

for key, value in ansDict.items():
    if(value != 0):
        ans += 1
maxValue = ans

for i in range(k, n):
    left = window.popleft()
    right = board[i]
    window.append(right)

    ansDict[left] -= 1
    if(ansDict[left] == 0):
        ans -= 1
    ansDict[right] += 1
    if(ansDict[right] == 1):
        ans += 1
    if(maxValue < ans):
        maxValue = ans

for i in range(k-1):
    left = window.popleft()
    right = board[i]
    window.append(right)

    ansDict[left] -= 1
    if(ansDict[left] == 0):
        ans -= 1
    ansDict[right] += 1
    if(ansDict[right] == 1):
        ans += 1
    if(maxValue < ans):
        maxValue = ans

print(maxValue)
