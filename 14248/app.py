from collections import deque

def bfs(start, stones):
    n = len(stones)
    visited = [False] * n
    queue = deque([start - 1])
    visited[start - 1] = True
    count = 1
    
    while queue:
        current = queue.popleft()
        
        # 왼쪽으로 점프
        if current - stones[current] >= 0 and not visited[current - stones[current]]:
            visited[current - stones[current]] = True
            queue.append(current - stones[current])
            count += 1
            
        # 오른쪽으로 점프
        if current + stones[current] < n and not visited[current + stones[current]]:
            visited[current + stones[current]] = True
            queue.append(current + stones[current])
            count += 1
            
    return count

# 입력 예시
n = int(input())
stones = list(map(int, input().split()))
s = int(input())

# 결과 출력
print(bfs(s, stones))