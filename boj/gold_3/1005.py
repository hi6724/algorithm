from collections import defaultdict,deque
'''
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4

120
건물은 1~N번까지 총 N개
'''

TC = int(input())
ans_list=[]
for i in range(TC):
  N,K = map(int,input().split(' '))
  income =list(map(int,input().split(" ")))
  root_costs=[0]
  costs=[0]
  costs.extend(income)
  root_costs.extend(income)

  graph=defaultdict(list)
  graph2=defaultdict(list)

  for i in range(K):
    x,y=map(int,input().split(" "))
    graph[x].append(y)
    graph2[y].append(x)
  end=int(input())
  q=deque()

  for i in range(1,N+1):
    if len(graph2[i])==0:
      q.append(i)

  while q:
    node=q.popleft() 
    cur_cost = costs[node]
    next_nodes=graph[node]
    for next_node in next_nodes:
      if root_costs[next_node]+cur_cost>costs[next_node]:
        costs[next_node]=root_costs[next_node]+cur_cost
        q.append(next_node)
  ans_list.append(costs[end])


for ans in ans_list:
  print(ans)
