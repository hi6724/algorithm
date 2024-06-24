from copy import deepcopy
N = int(input())
P = list(map(int,input().split(' ')))
S = list(map(int,input().split(' ')))

def hand_out_card(cur_card):
  global N,P,S
  temp=[[],[],[]]
  result = []
  for i in range(N):
    temp[i%3].append(cur_card[i])
  for l in temp:
    l.sort()
    result.append(l)
  return result

def shuffle_card(cur_card):
  global N,P,S
  new_card = deepcopy(cur_card)
  for i in range(N):
    new_card[S[i]]=cur_card[i]
  return new_card


target_list = [[],[],[]]
loop = hand_out_card([i for i in range(N)])
init_card = [i for i in range(N)]
for i in range(N):
  target_list[P[i]].append(i)




i = 0
while True:
  temp = hand_out_card(init_card)
  if temp == target_list:
    break
  if temp == loop and i > 0:
    i = -1
    break
  init_card=shuffle_card(init_card)
  i+=1
print(i)
