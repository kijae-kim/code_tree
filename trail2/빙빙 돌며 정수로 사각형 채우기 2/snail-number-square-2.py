# N과 M 입력받기
n, m = map(int, input().split())

# N x M 크기의 2차원 리스트를 0으로 초기화
arr = [[0] * m for _ in range(n)]

# 이동 방향 정의: 아래, 오른쪽, 위, 왼쪽
# (행, 열) 기준 이동량
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r, c = 0, 0  # 시작 위치 (0, 0)
dir_num = 0  # 방향 인덱스 (0: 아래, 1: 오른쪽, 2: 위, 3: 왼쪽)

# 1부터 N * M까지 숫자를 채우기
for i in range(1, n * m + 1):
    arr[r][c] = i
    
    # 다음 이동할 위치 미리 계산
    nr, nc = r + dr[dir_num], c + dc[dir_num]
    
    # 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
    if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4
        nr, nc = r + dr[dir_num], c + dc[dir_num]
        
    r, c = nr, nc

# 결과 출력 (각 행의 원소를 공백으로 구분하여 출력)
for row in arr:
    print(*row)