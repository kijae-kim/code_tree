# 지름길의 개수, 고속도로의 길이
N, D = map(int, input().split())
# 지름길 시작위치, 도착위치, 길이
shortcut_lst = [list(map(int, input().split())) for _ in range(N)]

# 차를 타고 D km의 고속도로를 지나간다
# 고속도로는 길이 험하다
# 지름길이 존재한다
# 역주행을 할 수 없다
# 운전해야하는 거리의 최솟값을 구하라

move = 0        # 움직인 거리
cur_pos = 0     # 현재 위치

way = [i for i in range(D+1)]     # dp

# 길을 가, 목적지까지
for i in range(D+1):
    # 한칸씩 오는게 빠를 때
    if i > 0:
        way[i] = min(way[i], way[i-1] + 1)
    # 지름길을 발견했을 때
    for s, e, d in shortcut_lst:
        # 지름길의 도착점은 최대 길이를 넘을 수 없다.
        if s == i and e <= D:
            way[e] = min(way[e], way[i] + d)

print(way[D])