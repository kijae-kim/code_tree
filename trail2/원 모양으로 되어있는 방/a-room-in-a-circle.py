n = int(input()) #방의 개수
arr = [int(input()) for _ in range(n)]

# 원 모양의 N개의 방
# 1부터 N까지 시계 반대방향으로 번호가 매겨져 있다.
# 각 방에는 이웃한 두 개의 방으로 통하는 문이 있다.
# 사람들은 무조건 시계 반대방향으로 이동한다.

# 시작하는 방을 적절히 정했을 때,
# 각방에 정해진 인원이 들어가는데 까지의 거리의 합의 최솟값을 구해라
ans = float('inf')

# 1. 모든 방(0 ~ n-1)을 각각 시작점으로 가정해 본다
for start in range(n):
    total_dist = 0
    
    # 2. 시작점으로부터 k칸 떨어진 방을 순서대로 확인한다 (k: 0 ~ n-1)
    for k in range(n):
        room_idx = (start + k) % n
        # total_dist에 (방에 들어갈 인원 * 이동 거리 k)를 누적
        total_dist += arr[room_idx]*k
        
    # 3. 최솟값 갱신
    ans = min(ans, total_dist)

print(ans)