from collections import deque
# 양방향, dfs 와 bfs
def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1 # 방문 표시
    for n in adj[c]:
        if not v[n]: #방문하지 않았다면
            dfs(n)
def bfs(s):
    q= deque() #q 생성
    q.append(s) #q에 초기데이터 넣기
    ans_bfs.append(s)
    
    v[s]=1 # 방문 표시
    while q:
        q= q.popleft() #q에있는 데이터 추출
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] =1 
        


    
N,M,V=map(int,input().split()) # N,M,V 변수 입력
adj= [[] for _ in range(N+1)] # adj 구현


for _ in range(M): #dfs로 q삽입 (양방향)
    s,e = map(int,input().split())
    adj.append(s)
    adj.append(e)

for i in range(1, N+1):
    adj[i].sort()
v = [0]* (N+1) #adj 안 방문노드
ans_dfs=[]
dfs(V)
v = [0]* (N+1) #adj 안 방문노드
ans_bfs=[]
bfs(V)

print(*ans_dfs)
print(*ans_bfs)

