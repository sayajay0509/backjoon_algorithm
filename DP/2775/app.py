def solve(k, n):
    # dp 배열 초기화: 최대 층과 호수에 대해 계산하기 위한 2차원 리스트
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # 0층 설정: 0층 i호에는 i명이 산다
    for i in range(1, n + 1):
        dp[0][i] = i

    # 1층부터 k층까지 각 호수에 사는 사람 수 계산
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]

    # k층 n호에 사는 사람 수 반환
    return dp[k][n]

# 테스트 케이스 개수
t = int(input())
for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호
    print(solve(k, n))