
import sys
import math
input = sys.stdin.readline
n = int(input())
ratio = [[] for _ in range(n)]
mass = [0] * (n)
visited = [False] * n



##관계리스트 생성
common_multi = 1
for _ in range(n-1):
  a, b, p, q = map(int,input().split())
  ratio[a].append((b,p,q))
  ratio[b].append((a,q,p))
  common_multi *= ((p*q)//math.gcd(p,q))
mass[0] = common_multi

##비율에 맞춰 계산하기 위한 그래프 탐색
def DFS(r):
  visited[r] = True
  for i in ratio[r]:
    if not visited[i[0]]:
      mass[i[0]] = i[2] * mass[r] // i[1]
      DFS(i[0])

DFS(0)
##최대 공약수 구하기
greatest_common_divisor = mass[0]
for i in range(n):
  greatest_common_divisor = math.gcd(greatest_common_divisor,mass[i])

##최대공약수로 각 질량을 나눠줌
for i in range(len(mass)):
  mass[i] = mass[i] // greatest_common_divisor
print(*mass)