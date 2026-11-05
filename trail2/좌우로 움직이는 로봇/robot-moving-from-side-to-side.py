n, m = map(int, input().split())

# Process robot A's movements
t_a = []
d_a = []
for _ in range(n):
    time, direction = input().split()
    t_a.append(int(time))
    d_a.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

MAX_CNT = 50000
MAX_TIME = 2000000

A = [0]
B = [0]

pos_a = 0
pos_b = 0

# 움직임 기록을 어떻게 해야하지?
# 리스트로 만들어서 인덱스 번호를 초로 생각하고 값으로 초단위 위치를 기록.
for i in range(n):
    time = t_a[i]
    dir = d_a[i]
    for t in range(time):
        if dir == 'L':
            pos_a -= 1
            A.append(pos_a)
        elif dir == 'R':
            pos_a += 1
            A.append(pos_a)

for i in range(m):
    time = t_b[i]
    dir = d_b[i]
    for t in range(time):
        if dir == 'L':
            pos_b -= 1
            B.append(pos_b)
        elif dir == 'R':
            pos_b += 1
            B.append(pos_b)

# A와 B가 움직이는 시간이 달라
# 예제는 B의 이동시간이 더 길다
B_length = len(B)
A_length = len(A)
# 비교 길이를 맞춰준다?
# 
if B_length > A_length:
    GAP = B_length - A_length

    for _ in range(GAP):
        A.append(A[-1])
    
    cnt = 0

    for i in range(1, B_length):
        if A[i-1] != B[i-1] and A[i] == B[i]:
            cnt += 1
    print(cnt)

elif A_length > B_length:
    GAP = A_length - B_length

    for _ in range(GAP):
        B.append(B[-1])
    
    cnt = 0

    for i in range(1, A_length):
        if A[i-1] != B[i-1] and A[i] == B[i]:
            cnt += 1
    print(cnt)
else:
    cnt = 0

    for i in range(1, A_length):
        if A[i-1] != B[i-1] and A[i] == B[i]:
            cnt += 1
    print(cnt)
