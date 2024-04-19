a, b, c, d, e = map(int, input().split())  # 입력값을 정수로 변환
sum_value = a**2 + b**2 + c**2 + d**2 + e**2  # 각 수의 제곱의 합 계산
ans = sum_value % 10  # 합을 10으로 나눈 나머지
print(ans)  # 결과 출력