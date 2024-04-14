n, m = map(int, input().split())
grid = [input() for _ in range(m)]  # 올바르게 입력을 받음
visited = [[False] * n for _ in range(m)]
count = 0

def dfs(x, y):
    # 범위 검사와 방문 여부, '#'인지 확인
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '#' or visited[x][y]:
        return
    visited[x][y] = True
    # 8방향 탐색: 상, 하, 좌, 우, 대각선
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        dfs(x + dx, y + dy)

for x in range(m):
    for y in range(n):
        if grid[x][y] == '#' and not visited[x][y]:
            dfs(x, y)
            count += 1

print(count)