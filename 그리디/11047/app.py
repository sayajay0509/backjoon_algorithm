n, k = map(int, input().split())  # n은 동전의 종류 수, k는 목표 금액
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0  # 사용된 동전의 수
for coin in reversed(coins):  # 가장 큰 동전부터 처리
    if k == 0:
        break
    if coin > k:
        continue
    count += k // coin  # 해당 동전으로 만들 수 있는 최대 개수
    k %= coin  # 남은 금액 업데이트

print(count)