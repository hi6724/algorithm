# 1205
n, my_score, p = map(int, input().split())
if n > 0:
    score = list(map(int, input().split()))
    score.append(my_score)
    score.sort(reverse=True)
    idx = score.index(my_score) + 1
    if idx > p:
        print(-1)
    else:
        if n == p and my_score == score[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)