n = int(input())
dp = [1] * 10  # 각 숫자로 끝나는 1자리 오르막 수의 개수는 1로 초기화

for _ in range(n - 1):
    for j in range(1, 10):
        dp[j] += dp[j - 1]  # j로 끝나는 숫자의 개수를 누적

ans = sum(dp)  # 길이 n의 오르막 수의 총 개수는 dp 배열의 모든 항목의 합
print(ans % 10007)