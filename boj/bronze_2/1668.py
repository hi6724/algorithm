n = int(input())
trophy = []
for i in range(n):
    trophy.append(int(input()))
left = [trophy[0], 1]
right = [trophy[-1], 1]
for i in range(1, len(trophy)):
    if trophy[i] > left[0]:
        left[0] = trophy[i]
        left[1] += 1
trophy.reverse()
for i in range(1, len(trophy)):
    if trophy[i] > right[0]:
        right[0] = trophy[i]
        right[1] += 1
print(left[1])
print(right[1])
