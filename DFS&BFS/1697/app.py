def bfs(s,e):
    # [1] 큐, v[], 필요 변수 생성
    q= []
    v = [0]*200001
    # [2] 초기데이터 삽입, v[] 초기화
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == e:
            return v[e]-1

        # 3방향, 범위내(0~20000), 미방문
        for n in (c-1,c+1,c*2):
            if 0<= n<200000 and v[n] ==0:
                q.append(n)
                v[n] = v[v]+1

    # 이곳에 도달할리는 없지만...
    return -1 

N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)