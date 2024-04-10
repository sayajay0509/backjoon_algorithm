n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# DFS 함수 정의
def dfs(x, y, color, is_blind):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
        return
    if is_blind and color in "RG":
        if grid[x][y] not in "RG":
            return
    elif grid[x][y] != color:
        return
    
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(x + dx, y + dy, color, is_blind)

# 구역 수를 세는 함수
def count_areas(is_blind=False):
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, grid[i][j], is_blind)
                count += 1
    return count

# 적록색약이 아닌 사람
normal = count_areas()

# 방문 기록 초기화
visited = [[False] * n for _ in range(n)]

# 적록색약인 사람
blind = count_areas(True)

print(normal, blind)