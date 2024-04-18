from collections import deque

def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1  # 시작점 방문 표시, 거리를 1로 설정

    while q:
        ci, cj = q.popleft()  # 큐에서 원소 제거
        if (ci, cj) == (ei, ej):  # 목표 위치에 도달한 경우
            return v[ei][ej]  # 시작 위치를 1로 시작했으므로 거리 직접 반환

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 4 방향 이동
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1  # 이전 경로에서 1 증가한 거리를 저장

# 입력 처리
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = bfs(0, 0, N - 1, M - 1)
print(ans)