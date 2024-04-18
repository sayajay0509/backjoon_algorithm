import sys
sys.stdin = open("input.txt", "r")

def bfs(si, sj):
    q =[] #q등 필요 변수 생성
    q.append((si,sj)) # 큐 초기데이터 삽입
    v[si][sj]= 1 # 방문 표시
    cnt =1 #정답처리 관련 작업

    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 4방향, 범위내, 미방문, 1이면 q 삽입
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _in range(N)]
ans =[]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] ==0:
            ans.append(bfs(i,j))


ans.sort()
print(len(ans), *ans, sep='\n')