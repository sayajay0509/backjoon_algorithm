matrix = [list(map(int, input().split())) for _ in range(9)]

# 최대값과 위치 초기화
max_value = -1
max_row = -1
max_col = -1

# 9x9 행렬 순회
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

# 최대값과 위치 출력 (행과 열 번호는 1부터 시작하므로 +1을 해줍니다)
print(max_value)
print(max_row + 1, max_col + 1)