import sys
input = sys.stdin.read

def solve(n):
    # dp 배열 초기화
    dp = [0] * (max(n) + 1)
    
    # 초기 조건 설정
    if 1 <= len(dp):
        dp[1] = 1
    if 2 <= len(dp):
        dp[2] = 2
    if 3 <= len(dp):
        dp[3] = 4

    # 점화식을 이용한 dp 배열 채우기
    for i in range(4, max(n) + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    # 각 n에 대한 결과 반환
    return [dp[x] for x in n]

# 테스트 케이스 개수와 각 n 입력 받기
data = input().split()
t = int(data[0])
cases = [int(data[i]) for i in range(1, t + 1)]

# 결과 출력
results = solve(cases)
for result in results:
    print(result)