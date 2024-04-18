from collections import deque
import sys
input = sys.stdin.read

def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]
    cnt = 0  # 익지 않은 토마토의 수

    # 큐 초기화 및 안 익은 토마토 수 계산
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:  # 익은 토마토
                    q.append((h, i, j))
                elif arr[h][i][j] == 0:  # 안 익은 토마토
                    cnt += 1

    if cnt == 0:
        return 0  # 모든 토마토가 이미 익어 있으면 0을 반환

    days = 0
    while q:
        ch, ci, cj = q.popleft()
        for dh, di, dj in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]:
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
                arr[nh][ni][nj] = 1
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                q.append((nh, ni, nj))
                cnt -= 1
                days = max(days, v[nh][ni][nj])  # 가장 오래 걸린 시간을 업데이트

    return -1 if cnt > 0 else days

# 입력 처리
data = input().split()
index = 0
M, N, H = map(int, data[index:index+3])
index += 3
arr = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, data[index:index+M])))
        index += M
    arr.append(layer)

# BFS 실행 후 결과 출력
result = bfs()
print(result)