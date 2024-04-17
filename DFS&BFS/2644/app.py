from sys import stdin
from collections import deque

def bfs(start, end, graph, visited):
    queue = deque([start])
    visited[start] = 0  # 시작 노드의 촌수는 0
    while queue:
        current = queue.popleft()
        if current == end:
            return visited[current]  # 목표 노드에 도달하면 촌수 반환
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    return -1  # 연결되지 않았다면 -1 반환

# 입력 처리
n = int(stdin.readline())  # 전체 사람 수
a, b = map(int, stdin.readline().split())  # 계산해야 할 두 사람의 번호
m = int(stdin.readline())  # 관계의 수

# 그래프 구성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 배열, 모든 노드는 방문하지 않은 상태(-1)로 초기화
visited = [-1] * (n + 1)

# BFS 실행 및 결과 출력
print(bfs(a, b, graph, visited))