from collections import deque

N, M = map(int, input().split())
floor = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 널빤지의 방향에 따른 탐색 방향 설정
directions = {'-': [(0, 1), (0, -1)], '|': [(1, 0), (-1, 0)]}

def bfs(x, y, direction):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions[direction]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and floor[nx][ny] == direction:
                visited[nx][ny] = True
                queue.append((nx, ny))

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, floor[i][j])
            count += 1

print(count)