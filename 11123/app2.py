from collections import deque

# 상, 하, 좌, 우 및 대각선 방향 이동을 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 8방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and area[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 입력 받기
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0

# 보드 순회하며 BFS 수행
for i in range(n):
    for j in range(m):
        if area[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

# 결과 출력
print(count)