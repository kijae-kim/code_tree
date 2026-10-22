from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 특정 제한값(limit) 이하의 돌만 밟고 n-1번째 돌에 도달할 수 있는지 확인하는 함수
def possible(limit):
    # 시작점이나 도착점이 제한값보다 크면 애초에 불가능
    if arr[0] > limit or arr[n - 1] > limit:
        return False
        
    visited = [False] * n
    queue = deque([0])
    visited[0] = True
    
    while queue:
        curr = queue.popleft()
        
        # 목적지에 도달했다면 성공
        if curr == n - 1:
            return True
            
        # 1부터 k칸까지 점프
        for i in range(1, k + 1):
            nxt = curr + i
            if nxt < n and not visited[nxt] and arr[nxt] <= limit:
                visited[nxt] = True
                queue.append(nxt)
                
    return False

# 이분 탐색 범위 설정
low = min(arr)
high = max(arr)
ans = high

while low <= high:
    mid = (low + high) // 2
    
    if possible(mid):
        ans = mid       # 가능하다면 더 작은 최댓값을 탐색하기 위해 범위를 줄임
        high = mid - 1
    else:
        low = mid + 1   # 불가능하다면 허용 최댓값을 늘림

print(ans)