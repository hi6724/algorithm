score1 = [(i)*2 for i in range(21)]
score1.extend([0 for i in range(41)])

score2 = [0, 0, 0, 0, 0, 10, 13, 16, 19, 25, 30, 35, 40]
score2.extend([0 for i in range(41)])

score3 = [0 for _ in range(10)]
score3 .extend([20, 22, 24, 25, 30, 35, 40])
score3.extend([0 for i in range(41)])

score4 = [0 for _ in range(15)]
score4 .extend([30, 28, 27, 26, 25, 30, 35, 40])
score4.extend([0 for i in range(41)])
scores = [score1, score2, score3, score4]

moves = list(map(int, input().split(' ')))

# 25 30 35 40
nestNode1 = [[1, 9], [2, 13], [3, 19]]
nestNode2 = [[1, 10], [2, 14], [3, 20]]
nestNode3 = [[1, 11], [2, 15], [3, 21]]
nestNode4 = [[1, 12], [2, 16], [3, 22], [0, 20]]

nestNodes = [nestNode1, nestNode2, nestNode3, nestNode4]


maxScore = 0


def n_bin(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(str):
    total = 0
    knights = [[0, 0], [0, 0], [0, 0], [0, 0]]

    for i in range(10):
        curKnight = knights[int(str[i])]
        curKnight[0] += moves[i]

        if curKnight[0] == 5 and curKnight[1] == 0:
            curKnight[1] = 1
        elif curKnight[0] == 10 and curKnight[1] == 0:
            curKnight[1] = 2
        elif curKnight[0] == 15 and curKnight[1] == 0:
            curKnight[1] = 3

        if curKnight[1] == 3 and curKnight[0] > 18:
            curKnight[1] = 1
            curKnight[0] -= 10
        if curKnight[1] == 2 and curKnight[0] > 12:
            curKnight[1] = 1
            curKnight[0] -= 4
        if curKnight[1] == 1 and curKnight[0] > 11:
            curKnight[1] = 0
            curKnight[0] += 8

        for j in range(4):
            if j != int(str[i]) and knights[j][0] == curKnight[0]:
                if scores[curKnight[1]][curKnight[0]] != 0 and knights[j][1] == curKnight[1]:
                    return -1

        total += scores[curKnight[1]][curKnight[0]]
    return total


for num in range(0, 4**9):
    cnt = 0
    temp1 = ''
    temp = n_bin(num, 4)
    for i in range(10-len(temp)):
        temp1 += '0'
    temp = temp1+temp
    tempScore = solution(temp)
    if tempScore > maxScore:
        maxScore = tempScore
print(maxScore)

'''
1 2 3 4 1 2 3 4 1 2
'''
# testCase = "0010222022"
# solution(testCase)
