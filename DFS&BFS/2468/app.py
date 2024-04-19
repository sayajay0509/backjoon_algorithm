N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
ans=0
for h in range(100):
    v=[[0]* N for _ in range(N)]
    ans=max(ans,solve(h))

print(ans)