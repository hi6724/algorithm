n = int(input())
home_list = []
for i in range(n):
    temp = list(input())
    home_list.append(list(map(int, temp)))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = []
ans = []
for i in range(n):
    for j in range(n):
        next_node = [[i, j]]
        cnt = 0
        while next_node:
            node = next_node.pop()
            if node not in visited and home_list[node[0]][node[1]] == 1:
                visited.append([node[0], node[1]])
                cnt += 1
                for k in range(4):
                    x = node[0] + dx[k]
                    y = node[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n:
                        next_node.append([x, y])
        if cnt > 0:
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in ans:
    print(i)