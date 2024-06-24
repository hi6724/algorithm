# 백준 1339 그리디
# https://hangjastar.tistory.com/216 반례
n = int(input())
words = []
temp = []
temp_dict = {}
for i in range(n):
    words.append(input())
words.sort(key=lambda x: -len(x))
for word in words:
    for i in range(len(word)):
        try:
            temp_dict[word[i]] += 10**(len(word) - i)
        except:
            temp_dict[word[i]] = 10**(len(word) - i)
word_dict = (list(temp_dict.items()))
word_dict.sort(key=lambda x: -x[1])
for i in range(len(word_dict)):
    temp_dict[word_dict[i][0]] = 9 - i
ans = ''
for word in words:
    temp = ''
    for i in range(len(word)):
        temp += str(temp_dict[word[i]])
    ans += temp + "+"
print(eval(ans[:-1]))
