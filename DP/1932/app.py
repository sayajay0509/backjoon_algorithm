import sys
input = sys.stdin.read

def solve(triangle):
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]
    
    # 초기화
    dp[0][0] = triangle[0][0]
    
    # DP 테이블 채우기
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    # 최대 합 찾기
    return max(dp[n-1])

# 입력 받기
data = input().split()
n = int(data[0])
triangle = [list(map(int, data[i*(i+1)//2 + 1:(i+1)*(i+2)//2 + 1])) for i in range(n)]

# 문제 해결 및 결과 출력
print(solve(triangle))