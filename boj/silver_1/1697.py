from collections import deque

MAX = 100001
n, k = map(int, input().split())

ans = {n: 0}
visited = []
need_visited = [n]
while need_visited:
    node = need_visited.pop(0)

    if k in ans:
        print(ans[k])
        break
    if node not in visited:
        for tt in (node - 1, node + 1, node * 2):
            if 0 <= tt < MAX and tt not in ans:
                ans[tt] = ans[node] + 1
                need_visited.append(tt)
        visited.append(node)
        # need_visited.extend([node - 1, node + 1, node * 2])

    # print(need_visited)
    # print(visited)
    # print(ans)
# print(arr[k])