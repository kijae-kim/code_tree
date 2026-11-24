from collections import deque

N = int(input())
num_list = list(map(int, input().split()))
A, B = map(int, input().split())

# 징검다리에서 점프를 할 때,
# 그 징검다리에 쓰여있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.

# A번째에서 B까지 가려고함
# 시작점에서 최소 몇번 점프를 해야 B까지 도달할 수 있을까?

ans = -1

# init
start = (A, 0)      # (현재 징검다리 번호, 지금까지 점프 횟수)
q = deque([start])
visited = [False] * (N + 1)
visited[A] = True

while q:
    curr_idx, cnt = q.popleft()

    if curr_idx == B:
        ans = cnt
        break

    step = num_list[curr_idx-1]

    if step > 0:
        for next_idx in range(curr_idx + step, N+1, step):
            if not visited[next_idx]:
                visited[next_idx] = True
                q.append((next_idx, cnt + 1))

        for next_idx in range(curr_idx - step, 0, -step):
            if not visited[next_idx]:
                visited[next_idx] = True
                q.append((next_idx, cnt + 1))
                
print(ans)