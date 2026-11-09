n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# 방향 정의: 오른쪽, 아래, 왼쪽, 위 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0  # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위

arr[x][y] = 1

for i in range(2, n * m + 1):
    # 현재 방향으로 다음 칸 확인
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    
    # 범위를 벗어나거나 이미 채워져 있는 경우 시계방향으로 90도 회전
    if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        
    arr[nx][ny] = i
    x, y = nx, ny

# 결과 출력
for row in arr:
    print(*row)