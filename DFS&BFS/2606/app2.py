from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return count - 1  # 1번 컴퓨터 자체는 제외하고 감염된 컴퓨터 수만 반환

# 입력 받기
n = int(input())  # 컴퓨터의 수
m = int(input())  # 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]  # 그래프 초기화

# 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 배열 초기화
visited = [False] * (n + 1)

# BFS 실행
result = bfs(1)
print(result)