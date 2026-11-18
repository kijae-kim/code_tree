# 19x19 바둑판 상태 입력 받기
board = [list(map(int, input().split())) for _ in range(19)]

# 4가지 방향 탐색: 우(→), 하(↓), 우하(↘), 우상(↗)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def solve():
    for x in range(19):
        for y in range(19):
            # 돌이 놓여 있는 칸일 경우에만 탐색
            if board[x][y] != 0:
                color = board[x][y]
                
                for i in range(4):
                    # 육목(6개 이상) 및 중복 방지: 시작 방향의 바로 뒷칸에 같은 색이 있으면 스킵
                    nx = x - dx[i]
                    ny = y - dy[i]
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                        continue
                    
                    # 현재 방향으로 연속된 돌의 개수 세기
                    cnt = 1
                    cx = x + dx[i]
                    cy = y + dy[i]
                    
                    while 0 <= cx < 19 and 0 <= cy < 19 and board[cx][cy] == color:
                        cnt += 1
                        cx += dx[i]
                        cy += dy[i]
                    
                    # 정확히 5개가 연속된 경우
                    if cnt == 5:
                        print(color)
                        # 5개 중 가운데(3번째) 돌의 좌표 계산 (시작점에서 해당 방향으로 2칸 이동)
                        mid_x = x + 2 * dx[i]
                        mid_y = y + 2 * dy[i]
                        print(mid_x + 1, mid_y + 1)  # 1부터 시작하는 좌표로 출력
                        return

    # 승부가 나지 않은 경우
    print(0)

solve()