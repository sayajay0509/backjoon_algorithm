n, m = map(int, input().split())  # n: 열의 수, m: 행의 수
grid = [list(map(int, input().split())) for _ in range(m)]  # m번 행을 입력받음
visited = [[False] * n for _ in range(m)]  # 방문 배열, m행 n열
count = 0

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
        return
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4방향 탐색
    for dx, dy in directions:
        dfs(x + dx, y + dy)

for x in range(m):
    for y in range(n):
        if grid[x][y] == 1 and not visited[x][y]:
            dfs(x, y)
            count += 1  # 연결된 영역 카운트
print(count)