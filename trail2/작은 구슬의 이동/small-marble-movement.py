N, T = map(int, input().split())
R, C, D = input().split()
R, C = int(R), int(C)

# 특정 방향으로 1초에 한칸씩 움직인다
# 이동 방향이 벽이라면 1초동안 방향을 반대로 바꾼다.
# 예시) Left ->> Right [1sec]
# 초기 방향이 주어졌을 때 T초가 지난 이후 구슬의 위치를 구해라

dim = [[0] * N for _ in range(N)]
# 초기값
cur_i, cur_j = R-1, C-1

def dir_setting(dir):
    # 방향을 입력하면 다음 움직일 델타값을 리턴
    if dir == 'R':
        return (0, 1)
    elif dir == 'L':
        return (0, -1)
    elif dir == 'D':
        return (1, 0)
    elif dir == 'U':
        return (-1, 0)
# 방향 전환
def reverse_dir(dir):
    if dir == 'R':
        return 'L'
    elif dir == 'L':
        return 'R'
    elif dir == 'D':
        return 'U'
    elif dir == 'U':
        return 'D'

for _ in range(T):
    di, dj = dir_setting(D)
    ni, nj = cur_i + di, cur_j + dj
    if 0 <= ni < N and 0 <= nj < N:
        cur_i, cur_j = ni, nj
    else:
        D = reverse_dir(D)

print(cur_i+1, cur_j+1)
