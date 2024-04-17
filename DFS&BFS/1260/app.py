from sys import stdin
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in sorted(graph[v]):
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_v in sorted(graph[current]):
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

# 입력 처리
n, m, v = map(int, stdin.readline().split())  # 노드 수, 간선 수, 시작 노드
graph = [[] for _ in range(n + 1)]

# 그래프 구성
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
visited = [False] * (n + 1)
dfs(v)
print()

# BFS
visited = [False] * (n + 1)
bfs(v)
print()