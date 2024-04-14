expression = input()

# '-'를 기준으로 식을 분할
parts = expression.split('-')

# 첫 번째 부분은 무조건 더하기
result = sum(map(int, parts[0].split('+')))

# 첫 '-' 이후의 각 부분에 대해 처리
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

# 결과 출력
print(result)