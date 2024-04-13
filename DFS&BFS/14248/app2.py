def dfs(start, stones):
    n = len(stones)
    visited = [False] * n
    stack = [start - 1]  # 시작 위치는 0-based index
    visited[start - 1] = True
    count = 1

    while stack:
        current = stack.pop()
        
        # 왼쪽으로 점프 가능한 경우
        left_jump = current - stones[current]
        if left_jump >= 0 and not visited[left_jump]:
            visited[left_jump] = True
            stack.append(left_jump)
            count += 1
        
        # 오른쪽으로 점프 가능한 경우
        right_jump = current + stones[current]
        if right_jump < n and not visited[right_jump]:
            visited[right_jump] = True
            stack.append(right_jump)
            count += 1

    return count

# 입력 예시
n = int(input())
stones = list(map(int, input().split()))
s = int(input())

# 결과 출력
print(dfs(s, stones))