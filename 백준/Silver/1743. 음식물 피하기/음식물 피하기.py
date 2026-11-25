# 세로 길이, 가로 길이, 음식물 쓰레기의 개수
N, M, K = map(int, input().split())
# 식당 그리드
cafeteria = [['.'] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# K개의 음식물 좌표
for k in range(K):
    r, c = map(int, input().split())
    cafeteria[r-1][c-1] = '#'

ans = 0

for n in range(N):
    for m in range(M):
        cnt = 0
        # 음식물이 있으면 주변에 음식물이 있는지 확인해
        if cafeteria[n][m] == '#':
            stack = [(n, m)]
            visited[n][m] = True
            while stack:
                x, y = stack.pop()
                cnt += 1
                # 상하좌우로 탐색
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and cafeteria[nx][ny] == '#' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            ans = max(ans, cnt)

print(ans)