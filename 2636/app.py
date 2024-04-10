from collections import deque

# 상, 하, 좌, 우 방향 이동을 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    cheese = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    board[nx][ny] = 0
                    cheese += 1
                visited[nx][ny] = True

    return cheese

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 0
last_cheese = 0

while True:
    cheese = bfs()
    if cheese == 0:
        break
    last_cheese = cheese
    time += 1

print(time)
print(last_cheese)