from collections import  deque

N,M,V = map(int,input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
dfs_visited = [False for _ in range(N+1)]
bfs_visited = [False for _ in range(N+1)]
dfs_result = []
bfs_result = []
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    dfs_visited[V] = True
    dfs_result.append(V)
    for i in range(1,N+1):
        if graph[V][i] == 1 and not dfs_visited[i]:
            dfs(i)


def bfs(V):
    bfs_visited[V] = True
    bfs_result.append(V)
    q = deque([V])
    while(q):
        x = q.popleft()
        for i in range(1,N+1):
            if graph[x][i] == 1 and not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = True
                bfs_result.append(i)

dfs(V)
bfs(V)


print(' '.join(map(str,dfs_result)))
print(' '.join(map(str,bfs_result)))
