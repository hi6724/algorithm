
import math

def sol():
  N = int(input())
  income = []
  if N == 1:
    print(1)
    return
  
  for i in range(N-1):
    a,b,p,q = map(int,input().split(' '))
    income.append([a,b,p,q])
    
  income.sort()
  init_value = 2
  values=[0 for _ in range(N)]
  # 모든 비율을 곱해서 무조건 공배수의 형태로 만듬
  for row in income:
    values[row[0]] = 1
    values[row[1]] = 1
    init_value=init_value*row[-1]*row[-2]
  values[income[0][0]]=init_value

  # 1이 존재하지 않을 때 까지 반복
  is_finish = False
  while not is_finish:
    for row in income:
      a,b,p,q = row
      if values[a]!=1 and values[b]!=1:
        continue
      # a가 1이 아니면 b는 a*q/p <- 무조건 자연수
      elif values[a] != 1:
        values[b] = values[a]*q//p
      elif values[b] != 1:
        values[a] = values[b]*p//q
    
    # 모든 값이 1이 아니면 멈춤
    is_finish = True
    for i in range(N):
      if values[i] == 1:
        is_finish = False

  # values배열의 최대 공약수를 구함
  gcd = values[0]
  for i in range(1,N):
    gcd = math.gcd(gcd,values[i])

  # 모든 값을 최대 공약수로 나누면 정답
  ans = ''
  for value in values:
    ans+=str(value//gcd)+' '
  print(ans.rstrip())
sol()