N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# 8가지 방향 탐색 (상, 하, 좌, 우, 좌상, 좌하, 우상, 우하)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

ans = 0

for x in range(N):
    for y in range(M):
        # 'L' 또는 'E'로 시작할 때 (문제 조건에 따라 'L'만 검사할 수도 있습니다)
        if grid[x][y] == 'L' or grid[x][y] == 'E':
            
            # 8가지 각 방향에 대해 3글자 단어 만들기
            for i in range(8):
                nx1 = x + dx[i]
                ny1 = y + dy[i]
                nx2 = x + 2 * dx[i]
                ny2 = y + 2 * dy[i]
                
                # 3칸 모두 격자 범위 내에 있는지 확인
                if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                    # 해당 방향으로 3글자 조합
                    word = grid[x][y] + grid[nx1][ny1] + grid[nx2][ny2]
                    
                    # 만약 완성된 단어가 "LEE"라면 카운트 증가
                    if word == "LEE":
                        ans += 1

print(ans)