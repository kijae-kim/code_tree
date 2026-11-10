N, M = map(int, input().split())

# A의 시간별 위치 기록
A = []
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        A.append(v)

# B의 시간별 위치 기록
B = []
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        B.append(v)

T = len(A)

pos_a = 0
pos_b = 0
ans = 0

# 초기 시작 시점(0초)에는 둘 다 위치가 0으로 같으므로 'BOTH'로 시작합니다.
current_leader = 'BOTH'

for i in range(T):
    pos_a += A[i]
    pos_b += B[i]
    
    # 현재 시점의 리더 판정
    if pos_a > pos_b:
        new_leader = 'A'
    elif pos_b > pos_a:
        new_leader = 'B'
    else:
        new_leader = 'BOTH'
        
    # 리더가 직전과 달라졌다면 교체 횟수 증가
    if new_leader != current_leader:
        ans += 1
        current_leader = new_leader

print(ans)