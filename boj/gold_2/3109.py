import sys

input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

# 오른위 -> 오른 -> 오른아래
dx = [-1, 0, 1]
dy = [1, 1, 1]
count = 0
visited = [[0]*C for _ in range(R)]


def dfs(px, py):
    global count
    if py == C-1:
        count += 1
        return True

    for i in range(3):
        nx = px+dx[i]
        ny = py+dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and arr[nx][ny] == '.':
                visited[px+dx[i]][py+dy[i]] = 1
                if dfs(nx, ny):
                    return True
                    #이 부분에서 return과 return True 차이가 무엇인가요??

    return False


for i in range(R):
    dfs(i, 0)

print(count)
