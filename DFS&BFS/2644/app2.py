from collections import deque

def bfs(n):
    visited[n] = 1
    q = deque()
    q.append(n)
    while q:
        num = q.popleft()
        for i in adj[num]:
            if visited[i] == 0:
                visited[i] = visited[num] + 1
                q.append(i)
    return visited[person2]-1


N = int(input())
person1, person2 = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [0]* (N+1)

for i in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

print(bfs(person1))