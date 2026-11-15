def solve():
    # N(행)과 M(열) 입력 받기 (예: 4 2)
    line = input().split()
    if not line:
        return
    N = int(line[0])
    M = int(line[1])

    # N × M 크기의 2차원 리스트를 빈 문자열로 초기화
    grid = [["" for _ in range(M)] for _ in range(N)]

    # 이동 방향: 우, 하, 좌, 상 (시계 방향)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0  # 현재 위치 (행, 열)
    dir_idx = 0  # 현재 방향 인덱스 (0: 우, 1: 하, 2: 좌, 3: 상)

    # 'A'부터 시작하여 알파벳 순환 채우기
    current_char_code = ord("A")

    for _ in range(N * M):
        grid[x][y] = chr(current_char_code)

        current_char_code += 1
        if current_char_code > ord("Z"):
            current_char_code = ord("A")

        # 다음 이동할 위치 미리 계산
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        # 범위를 벗어나거나 이미 채워진 칸인 경우 방향 전환 (우 -> 하 -> 좌 -> 상)
        if (
            nx < 0
            or nx >= N
            or ny < 0
            or ny >= M
            or grid[nx][ny] != ""
        ):
            dir_idx = (dir_idx + 1) % 4
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]

        # 위치 갱신
        x, y = nx, ny

    # 결과 출력 (각 행의 원소를 공백으로 구분하여 출력)
    for row in grid:
        print(" ".join(row))


if __name__ == "__main__":
    solve()