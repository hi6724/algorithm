N, M = map(int, input().split(' '))

pattern1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]
pattern2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

patterns = [pattern1, pattern2]


def is_check(boards, x, y):
    match_pattern = patterns[0]
    cnt1 = 0
    for i in range(8):
        for j in range(8):
            if match_pattern[i][j] != boards[x+i][j+y]:
                cnt1 += 1

    match_pattern = patterns[1]
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if match_pattern[i][j] != boards[x+i][j+y]:
                cnt2 += 1

    return min(cnt1, cnt2)


boards = []
for i in range(N):
    boards.append(list(input()))

ans = []
for i in range(N-7):
    for j in range(M-7):
        cnt = is_check(boards, i, j)
        ans.append(cnt)
print(min(ans))
