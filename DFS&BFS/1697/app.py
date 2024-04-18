from collections import deque
import sys

input = sys.stdin.read

def bfs(s, e):
    # [1] 큐, v[], 필요 변수 생성
    q = deque()
    v = [0] * 200001  # 주어진 문제 조건에 맞게 범위 설정

    # [2] 초기데이터 삽입, v[] 초기화
    q.append(s)
    v[s] = 1  # 시작 지점의 방문을 표시하고, 거리를 1로 시작 (거리를 0이 아닌 1로 설정하는 이유는 최종 결과에서 1을 빼기 위함)

    while q:
        c = q.popleft()  # deque를 사용하여 효율적으로 요소 접근
        if c == e:
            return v[e] - 1  # 처음 v[s]를 1로 설정했으므로 결과에서 1을 빼준다.

        # 3방향, 범위 내 (0~200000), 미방문
        for n in (c - 1, c + 1, c * 2):
            if 0 <= n <= 200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1  # 이동 거리를 갱신

    # 이곳에 도달할 리는 없지만, 혹시 모르는 상황 대비
    return -1

# 입력 처리
N, K = map(int, input().split())
ans = bfs(N, K)
print(ans)