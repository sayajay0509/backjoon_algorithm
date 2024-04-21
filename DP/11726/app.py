N = int(input())
dp = [0] * (N + 1)

# N이 1보다 작은 경우를 처리하기 위해 조건문 추가
if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007  # 바로 모듈로 연산을 적용하여 오버플로우 방지

ans = dp[N]
print(ans)