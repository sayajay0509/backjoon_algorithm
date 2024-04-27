from collections import deque

def bfs(s, e):
    q = deque()  # deque로 큐 생성
    v = [0] * (N + 1)
    q.append(s)
    v[s] = 1
    while q:
        c = q.popleft()  # deque의 popleft를 사용하여 O(1) 시간 복잡도 보장
        if c == e:
            return v[e] - 1

        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] = v[c] + 1

    return -1

# 입력 받는 부분과 인접 리스트 생성
N = int(input("Enter the number of nodes: "))
S, E = map(int, input("Enter start and end nodes separated by space: ").split())
M = int(input("Enter the number of edges: "))
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    p, c = map(int, input("Enter connected nodes separated by space: ").split())
    adj[p].append(c)
    adj[c].append(p)

# BFS 실행 및 결과 출력
ans = bfs(S, E)
print(ans)