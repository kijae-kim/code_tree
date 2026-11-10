n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# safty = 인접한 칸 중 색칠되어 있는 칸이 3개인 경우.
# points의 (idx, T/F) 좌표에서 상하좌우에 색칠한 칸이 3개면 print(1) 아니면 print(0)
    # 색칠

grid = [[0] * n for _ in range(n)]

for i in range(m):
    i, j = points[i]
    i, j = i-1, j-1
    cozy = 0 

    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if grid[ni][nj] == 1:
                cozy += 1
    
    grid[i][j] = 1

    if cozy == 3:
        print(1)
    else:
        print(0)