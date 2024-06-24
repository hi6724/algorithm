import heapq

n = int(input())
card_list = []
for i in range(n):
    k = int(input())
    heapq.heappush(card_list, k)
ans = 0
while len(card_list) > 1:
    card1 = heapq.heappop(card_list)
    card2 = heapq.heappop(card_list)
    heapq.heappush(card_list, card1 + card2)
    ans += (card1 + card2)
print(ans)
