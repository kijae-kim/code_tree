from collections import deque

# maze
# N * M 크기의 미로
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 출력
# (0,0) ~ (M-1, N-1) 까지
# 지나야하는 최소 칸 수
ans = float('inf')

q = deque()
q.append((0, 0, 1))
visited[0][0] = True

while q:
    x, y, cnt = q.popleft()

    if x == N-1 and y == M-1:
        ans = min(ans, cnt)
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and maze[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))

print(ans)