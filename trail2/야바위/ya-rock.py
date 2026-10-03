n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# 3가지 시작 위치(1, 2, 3)에 대해 각각 얻을 수 있는 점수를 저장
scores = [0, 0, 0]

# 처음에 조약돌이 1, 2, 3 번 위치에 놓였을 때 각각의 현재 위치
pebble_pos = [1, 2, 3]

# N번의 연산을 순서대로 진행
for i in range(n):
    swap_a = a[i]
    swap_b = b[i]
    check_c = c[i]
    
    # 3가지 시나리오에 대해 각각 위치 변경 및 점수 체크
    for k in range(3):
        # swap_a와 swap_b 위치 교환
        if pebble_pos[k] == swap_a:
            pebble_pos[k] = swap_b
        elif pebble_pos[k] == swap_b:
            pebble_pos[k] = swap_a
            
        # 열어본 위치(check_c)에 조약돌이 있다면 1점 획득
        if pebble_pos[k] == check_c:
            scores[k] += 1

# 얻을 수 있는 최대 점수 출력
print(max(scores))