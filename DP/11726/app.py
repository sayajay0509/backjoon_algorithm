N = int(input())
dp=[0]*(N+1)
dp[0],dp[1]=1,1
for i in rage(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]*2
    
ans = dp(N)
print(ans%10007)