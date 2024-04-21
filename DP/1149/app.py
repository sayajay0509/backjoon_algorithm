import sys
input = sys.stdin.read

def solve(costs):
    n = len(costs)
    dp = [[0]*3 for _ in range(n)]

    # 초기 조건 설정
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]

    # DP를 이용하여 각 집을 칠하는 최소 비용 계산
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 집에서 모든 색상 중 최소 비용을 반환
    return min(dp[-1][0], dp[-1][1], dp[-1][2])

# 입력 받기
data = input().split()
n = int(data[0])
costs = [list(map(int, data[i*3+1:i*3+4])) for i in range(n)]

# 문제 해결 및 결과 출력
print(solve(costs))