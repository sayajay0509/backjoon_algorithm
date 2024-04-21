def min_operations(n):
    dp = [0] * (n + 1)  # dp 배열 초기화
    
    for i in range(2, n + 1):
        # 무조건 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

# 입력 받기
n = int(input())
print(min_operations(n))