from sys import stdin, setrecursionlimit

setrecursionlimit(100000)  # 파이썬의 기본 재귀 깊이 제한 확장

def dfs(x, y):
    global sheep, wolf
    if grid[x][y] == 'v':
        wolf += 1
    elif grid[x][y] == 'k':
        sheep += 1
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] != '#':
            dfs(nx, ny)

R, C = map(int, stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
total_sheep, total_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and grid[i][j] != '#':
            sheep, wolf = 0, 0
            dfs(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)