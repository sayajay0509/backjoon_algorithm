from collections import deque

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1000부터 9999까지의 모든 소수를 찾는 함수
def find_primes():
    return [i for i in range(1000, 10000) if is_prime(i)]

# 한 자리씩 변경하며 탐색 가능한 모든 숫자를 생성하는 함수
def possible_numbers(current):
    for i in range(4):
        for digit in '0123456789':
            if i == 0 and digit == '0':
                continue  # 첫 번째 자리는 0이 될 수 없음
            new_number = current[:i] + digit + current[i+1:]
            if is_prime(int(new_number)):
                yield new_number

# BFS를 사용한 최소 변환 횟수 찾기
def bfs(start, end):
    visited = {start: 0}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return visited[current]
        for next_number in possible_numbers(current):
            if next_number not in visited:
                visited[next_number] = visited[current] + 1
                queue.append(next_number)
    return "Impossible"

# 주어진 케이스에 대해 문제 해결
T = int(input())
for _ in range(T):
    start, end = input().split()
    result = bfs(start, end)
    print(result)