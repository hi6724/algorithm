from itertools import combinations
import math

N = int(input())
score_board = []
for i in range(N):
  score_board.append(list(map(int, input().split(' '))))
min_gap = math.inf
for team1 in combinations(range(N), N//2):
  team2 = [item for item in list(range(N)) if item not in team1]
  team1_score = 0
  team2_score = 0
  for player in team1:
    for player2 in team1:
      team1_score += score_board[player][player2]
  for player in team2:
    for player2 in team2:
      team2_score += score_board[player][player2]
  min_gap = min(min_gap, abs(team1_score-team2_score))
print(min_gap)
