n = int(input())  # n 입력 받기
a = list(map(int, input().split()))  # 리스트 a 입력 받기
b = list(map(int, input().split()))  # 리스트 b 입력 받기

# a는 오름차순으로 정렬
a.sort()

# b는 내림차순으로 정렬
b.sort(reverse=True)

# a와 b의 해당 요소를 곱한 값을 합산
sum = 0
for i in range(n):
    sum += a[i] * b[i]

# 결과 출력
print(sum)