from collections import deque

N = int(input())
maze = [input().strip() for _ in range(N)]
costs = [[float('inf') for _ in range(N)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque([(0, 0)])
    costs[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = costs[x][y] + (maze[nx][ny] == '0')  # 검은 방일 경우 비용 증가
                if next_cost < costs[nx][ny]:
                    costs[nx][ny] = next_cost
                    queue.append((nx, ny))
    return costs[N-1][N-1]

print(bfs())