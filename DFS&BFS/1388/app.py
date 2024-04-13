N, M = map(int, input().split())
floor = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y, direction):
    if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or floor[x][y] != direction:
        return
    visited[x][y] = True
    if direction == '-':
        dfs(x, y + 1, direction)
    else:  # direction == '|'
        dfs(x + 1, y, direction)

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, floor[i][j])
            count += 1

print(count)