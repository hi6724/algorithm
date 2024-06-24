from string import ascii_lowercase
from itertools import combinations


def sol():
    must_have = ['a', 'n', 't', 'i', 'c']
    alphabet_list = list(ascii_lowercase)
    for a in must_have:
        alphabet_list.remove(a)

    N, M = map(int, input().split(' '))
    words = []
    for i in range(N):
        alpha = set()
        word = input()[4:-4]
        for w in word:
            if w != 'a' and w != 'n' and w != 't' and w != 'i' and w != 'c':
                alpha.add(w)
        words.append(alpha)
    if M < 5:
        print(0)
        return
    ans = 0
    for comb in list(combinations(alphabet_list, M-5)):
        cnt = 0
        for word in words:
            is_ok = True
            for w in word:
                if w not in comb:
                    is_ok = False
                    break
            if is_ok:
                cnt += 1
        if cnt > ans:
            ans = cnt

    print(ans)


sol()
