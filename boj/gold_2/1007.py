from itertools import combinations
import math
TC = int(input())
for _ in range(TC):
  N = int(input())
  all_points = []
  total = [0, 0]
  ans = math.inf
  for __ in range(N):
    x, y = map(int, input().split(' '))
    total[0] += x
    total[1] += y
    all_points.append([x, y])
  end_points_list = list(combinations(all_points, N//2))
  for end_points in end_points_list:
    x1, y1 = 0, 0
    for end_point in end_points:
      x1 += end_point[0]
      y1 += end_point[1]
    x2, y2 = total[0]-x1, total[1]-y1
    vector_length = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
    ans = min(ans, vector_length)
  print(ans)
