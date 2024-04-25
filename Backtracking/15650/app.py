def dfs(start, lst):
    if len(lst) == M:  # M개짜리 수열이 완성된 경우
        ans.append(lst)
        return
    for i in range(start, N+1):
        dfs(i+1, lst + [i])  # 현재 숫자를 포함하는 경우, 다음 숫자는 현재 숫자 다음부터

N, M = map(int, input().split())
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)