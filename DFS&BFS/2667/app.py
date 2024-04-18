import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _in range(N)]
ans =[]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] ==0:
            ans.append(bfs(i,j))


ans.sort()
print(len(ans), *ans, sep='\n')