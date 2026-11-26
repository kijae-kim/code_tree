N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
max_area = -float('inf')
# 방문 표시
visited = [[False] * M for _ in range(N)]

# 1을 발견하면
for n in range(N):
    for m in range(M):
        if info[n][m] == 1 and visited[n][m] == False:
            cnt += 1        # 그림 발견
            area = 1
            stack = [(n, m)]
            visited[n][m] = True    # 방문 표시

            while stack:
                x, y = stack.pop()

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and info[nx][ny] == 1:     # 범위 체크
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        area += 1
                max_area = max(max_area, area)
if cnt == 0:
    print(0)
    print(0)
else:
    print(cnt)
    print(max_area)