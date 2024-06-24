from collections import defaultdict
from itertools import combinations
from copy import deepcopy

root_num,k = input().split(' ')
k = int(k)
ans = -1
visited=defaultdict(lambda:defaultdict(bool))

all_comb = list(combinations(range(len(root_num)),2))

def bfs(num_list,cnt):
  
  global all_comb,visited,ans
  num = ''.join(num_list)
  
  if num_list[0]=='0':
    return
  elif cnt == 0:
    ans = max(ans,int(num))
    return
  elif visited[num][cnt]:
    return
  
  visited[num][cnt] = True
  for a,b in all_comb:
    new_num_list = deepcopy(num_list)
    new_num_list[a],new_num_list[b]=new_num_list[b],new_num_list[a]
    bfs(new_num_list,cnt-1)
    
  

bfs(list(root_num),k)

print(ans)