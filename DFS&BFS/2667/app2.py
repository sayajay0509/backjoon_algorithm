from collections import deque
import sys
input = sys.stdin.read

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '1':
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

# 입력 처리
data = input().split()
N = int(data[0])  # 첫 줄에 N을 입력받음
grid = [list(data[i+1]) for i in range(N)]

visited = [[False] * N for _ in range(N)]
complexes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:
            complexes.append(bfs(i, j))

complexes.sort()
print(len(complexes))
for comp in complexes:
    print(comp)