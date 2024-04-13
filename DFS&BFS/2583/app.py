from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1  # 현재 영역의 크기
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area += 1
    return area

m, n, k = map(int, input().split())
grid = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

# 직사각형 영역을 1로 표시
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

areas = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            areas.append(bfs(i, j))

areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))