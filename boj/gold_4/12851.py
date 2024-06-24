visited = [0 for _ in range(100001)]
ansList = [0 for _ in range(100001)]

N, K = map(int, input().split(" "))
steps = [[N]]
index = 0
visited[N] = 1
ansList[N] = 1
delta = ["+1", "-1", "*2"]
isFinish = False
ans = 0
if N == K:
    isFinish = True
    ans = 1
while not isFinish:
    curs = set(steps[index][:])
    index += 1
    steps.append([])
    temp = []
    for cur in curs:
        for i in range(3):
            currentValue = eval(str(cur)+delta[i])
            if currentValue >= 100001:
                continue
            if currentValue == K:
                isFinish = True
                ans += ansList[cur]
            elif visited[currentValue] == 0 and currentValue > 0 and currentValue < 100001:
                steps[index].append(currentValue)
                ansList[currentValue] += ansList[cur]
                temp.append(currentValue)
    for value in temp:
        visited[value] = 1

print(len(steps)-1)
print(ans)
