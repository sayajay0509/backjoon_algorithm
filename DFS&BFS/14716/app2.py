n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
count = 0

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == 0 or visited[x][y]:
        return
    visited[x][y] = True
    # 8방향 탐색: 상, 하, 좌, 우, 대각선
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        dfs(x + dx, y + dy)

for x in range(m):
    for y in range(n):
        if board[x][y] == 1 and not visited[x][y]:
            dfs(x, y)
            count += 1
print(count)