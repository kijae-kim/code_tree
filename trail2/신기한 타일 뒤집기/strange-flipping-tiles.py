N = int(input())

# 최대 이동 가능 거리: 1000 * 100 = 100,000
OFFSET = 100000
# -10만 ~ +10만을 커버할 수 있는 배열 생성 (0: 미방문, 1: 흰색, 2: 검은색)
tiles = [0] * (OFFSET * 2 + 1)

curr = OFFSET  # 시작 위치를 중앙(100,000)으로 설정

for _ in range(N):
    x_str, direction = input().split()
    x = int(x_str)
    
    if direction == 'L':
        start = curr - x + 1
        end = curr
        for pos in range(start, end + 1):
            tiles[pos] = 1  # 1: 흰색
        curr = start
        
    elif direction == 'R':
        start = curr
        end = curr + x - 1
        for pos in range(start, end + 1):
            tiles[pos] = 2  # 2: 검은색
        curr = end

# 흰색(1)과 검은색(2) 개수 집계
white_cnt = tiles.count(1)
black_cnt = tiles.count(2)

print(white_cnt, black_cnt)