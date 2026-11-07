N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

def wsne(dir):
    if dir == 'N':
        return (1, 0)
    elif dir == 'S':
        return (-1, 0)
    elif dir == 'W':
        return (0, -1)
    elif dir == 'E':
        return (0, 1)


cur_x, cur_y = 0, 0
total_steps = 0
ans = -1  # 원점에 도달하지 못한 경우를 기본값 -1로 설정

for dir, bias in moves:
    bias = int(bias)
    di, dj = wsne(dir)
    
    for _ in range(bias):
        cur_x += di
        cur_y += dj
        total_steps += 1  # 전체 이동 횟수 누적
        
        # 처음으로 (0, 0)에 도달한 경우
        if cur_x == 0 and cur_y == 0:
            ans = total_steps
            break  # 첫 번째로 도달한 시점을 찾았으므로 종료
            
    if ans != -1:
        break  # 바깥 반복문도 종료

print(ans)