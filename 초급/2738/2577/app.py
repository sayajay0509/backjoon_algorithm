# 세 개의 수 입력받기
A = int(input())
B = int(input())
C = int(input())

# 세 수의 곱 계산
product = A * B * C

# 곱한 결과를 문자열로 변환
product_str = str(product)

# 0부터 9까지 각 숫자의 등장 횟수를 세기
for i in range(10):
    count = product_str.count(str(i))  # 문자열에서 특정 숫자의 등장 횟수를 세기
    print(count)  # 결과 출력