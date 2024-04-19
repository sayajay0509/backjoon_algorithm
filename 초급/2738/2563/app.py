paper = [[0]*100 for _ in range(100)]

# 색종이의 수 입력
n = int(input())

for _ in range(n):
    # 색종이의 왼쪽 하단 꼭짓점 좌표 입력
    x, y = map(int, input().split())
    # 색종이를 도화지에 붙이기 (10x10 크기의 색종이)
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1

# 도화지에서 색종이가 차지하는 면적 계산
area = sum(sum(row) for row in paper)
print(area)