'''
10 8
5 7 9 10 3 4 4 3
'''

N,M = map(int,input().split(' '))
incomes = list(map(int,input().strip().split(' ')))


papers=set()
needs=[]
for i in incomes:
    papers.add(i)

for i in range(1,N+1):
    if i not in papers:
        needs.append(i)

needs.sort()
if len(needs)==0:
    print(0)
else:
  ans = 0
  group=[]
  for need in needs:
      if len(group)==0:
          group.append(need)
      elif group[-1] + 3 >= need:
          group.append(need)
      else:
          ans+=5+(2*(max(group)-min(group)+1))
          group = [need]
  ans+=5+(2*(max(group)-min(group)+1))
  print(ans)