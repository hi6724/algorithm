test_case = int(input())
for i in range(test_case):
    row, column, k = map(int, input().split())
    arr = [[0 for __ in range(column + 1)] for _ in range(row + 1)]
    for i in range(k):
        w, h = map(int, input().split())
        arr[w][h] = 1

    visited = []
    hehe = []
    ans = 0
    for i in range(row):
        for j in range(column):
            need_visit = [[i, j]]
            temp = []
            while need_visit:
                node = need_visit.pop(0)
                if node not in visited and arr[node[0]][node[1]] == 1:
                    visited.append(node)
                    temp.append(node)
                    need_visit.extend([[node[0] + 1, node[1]],
                                       [node[0], node[1] + 1],
                                       [node[0] - 1, node[1]],
                                       [node[0], node[1] - 1]])
                    ans += 1
            if len(temp) > 0:
                hehe.append(temp)
    print(len(hehe))