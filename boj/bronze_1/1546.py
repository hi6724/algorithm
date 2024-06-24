input()
scores = list(map(int, input().split(' ')))
max_score = max(scores)
new_scores = []
for score in scores:
    new_score = (score/max_score)*100
    new_scores.append(new_score)
print(sum(new_scores)/len(new_scores))
