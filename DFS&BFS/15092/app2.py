from collections import deque

def input_grid(m):
    return [input().strip() for _ in range(m)]

def bfs(grid, visited, start_x, start_y, m, n):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_amoebas(m, n, grid):
    visited = [[False] * n for _ in range(m)]
    count = 0
    for x in range(m):
        for y in range(n):
            if grid[x][y] == '#' and not visited[x][y]:
                bfs(grid, visited, x, y, m, n)
                count += 1
    return count

# 입력 부분
m, n = map(int, input().split())
grid = input_grid(m)

# 결과 출력
print(count_amoebas(m, n, grid))