N, M = map(int, input().split())  # 행렬의 크기 입력

# 첫 번째 행렬 입력
matrix1 = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 행렬 입력
matrix2 = [list(map(int, input().split())) for _ in range(N)]

# 두 행렬의 덧셈 결과 저장을 위한 행렬
result = [[0]*M for _ in range(N)]

# 행렬 덧셈 수행
for i in range(N):
    for j in range(M):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# 결과 출력
for row in result:
    print(*row)