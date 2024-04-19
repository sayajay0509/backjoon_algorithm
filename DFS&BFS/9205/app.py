from collections import deque

def bfs(sj, si, ej, ei):
    # q 생성 및 필요 변수 초기화
    q = deque()
    v = [0] * N  # 방문 배열

    # 큐에 초기 데이터 삽입, 시작지점은 방문 표시 X
    q.append((sj, si))
    
    while q:
        cj, ci = q.popleft()  # deque 사용하여 O(1)로 pop
        if abs(cj - ej) + abs(ci - ei) <= 1000:  # 목적지 도달 가능
            return 'happy'
        
        # 미방문 모든 편의점 좌표: 범위 내인지 체크
        for i in range(N):
            if v[i] == 0:  # 미방문 편의점
                nj, ni = lst[i]
                if abs(cj - nj) + abs(ci - ni) <= 1000:
                    q.append((nj, ni))
                    v[i] = 1
                    
    return 'sad'        

TC = int(input())
for _ in range(TC):
    N = int(input())  # 편의점 수
    sj, si = map(int, input().split())  # 시작 좌표
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())  # 도착 좌표

    ans = bfs(sj, si, ej, ei)
    print(ans)