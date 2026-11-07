commands = input()

# 방향 정의: 북(0), 동(1), 남(2), 서(3) -> 시계 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 상태 설정 (북쪽을 바라보고 (0, 0)에서 시작)
x, y = 0, 0
curr_dir = 0
time = 0
ans = -1

for cmd in commands:
    time += 1  # L, R, F 상관없이 명령어 실행 시 1초 경과
    
    if cmd == 'L':
        curr_dir = (curr_dir - 1) % 4  # 반시계 방향 회전
    elif cmd == 'R':
        curr_dir = (curr_dir + 1) % 4  # 시계 방향 회전
    elif cmd == 'F':
        x += dx[curr_dir]
        y += dy[curr_dir]
    
    # 처음으로 (0, 0)에 돌아왔는지 확인
    if x == 0 and y == 0:
        ans = time
        break

print(ans)