from collections import defaultdict
cnt = defaultdict(int)
items = list(input().upper())

for el in items:
    cnt[el] += 1
list_items = list(cnt.items())
list_items.sort(key=lambda x: -x[1])

if len(list_items) <= 1:
    print(list_items[0][0])
elif list_items[0][1] == list_items[1][1]:
    print('?')
else:
    print(list_items[0][0])
