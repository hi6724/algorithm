import sys
input = sys.stdin.readline
from math import factorial
c = [(0,1),(1,2),(0,2)]

def combination(x,y):
  return factorial(x)//factorial(y)//factorial(x-y)

def DFS(n,cnt):
  global result
  if n == N+1:
    result += cnt
    return
  for i in range(3):
    if RGB[i] >= n:
      RGB[i] -= n
      DFS(n+1,cnt)
      RGB[i] += n
  if not n%2:
    for i,j in c:
      if RGB[i] >= n//2 and RGB[j] >= n//2:
        RGB[i] -= n//2
        RGB[j] -= n//2
        DFS(n+1,cnt*combination(n,n//2))
        RGB[i] += n//2
        RGB[j] += n//2
  if not n%3:
    if RGB[0] >= n//3 and RGB[1] >= n//3 and RGB[2] >= n//3:
      for i in range(3):
        RGB[i] -= n//3
      DFS(n+1,cnt*combination(n,n//3)*combination(n-n//3,n//3))
      for i in range(3):
        RGB[i] += n//3 

N,R,G,B = map(int,input().split())
RGB = [R,G,B]

result = 0
DFS(1,1)
print(result)
