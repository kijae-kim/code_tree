n, m = map(int, input().split())

# A의 시간별 위치 기록
A = []
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        A.append(v)

# B의 시간별 위치 기록
B = []
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        B.append(v)

# 누적 거리 계산을 위한 배열 (0초 시점인 0을 포함하거나 초 단위로 순회)
a_pos = 0
b_pos = 0

ans = 0
leader = 0  # 0: 없음/시작전, 1: A가 선두, 2: B가 선두

# 총 시간 동안 1초씩 이동하며 확인
for i in range(len(A)):
    a_pos += A[i]
    b_pos += B[i]
    
    current_leader = 0
    if a_pos > b_pos:
        current_leader = 1
    elif a_pos < b_pos:
        current_leader = 2
    
    # 최초 선두가 정해지거나, 기존 선두와 달라졌을 때 (단, leader가 0이 아닐 때부터 변경 횟수 카운트 혹은 첫 리드 인정 방식 고려)
    # 문제 조건: "어느 한 쪽이 앞서가기 전까지는 선두가 바뀌지 않았다고 판단합니다."
    if current_leader != 0 and leader == 0:
        leader = current_leader
    elif current_leader != 0 and current_leader != leader:
        ans += 1
        leader = current_leader

print(ans)