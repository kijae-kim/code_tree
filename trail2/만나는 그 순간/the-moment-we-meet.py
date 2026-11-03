n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# A의 초당 위치를 기록 (시작점 0초일 때 위치는 0)
pos_a = [0]
curr = 0
for i in range(n):
    direction = d[i]
    time = t[i]
    for _ in range(time):
        if direction == 'R':
            curr += 1
        else:
            curr -= 1
        pos_a.append(curr)

# B의 초당 위치를 기록 (시작점 0초일 때 위치는 0)
pos_b = [0]
curr = 0
for i in range(m):
    direction = d2[i]
    time = t2[i]
    for _ in range(time):
        if direction == 'R':
            curr += 1
        else:
            curr -= 1
        pos_b.append(curr)

# 1초부터 시작하여 처음으로 위치가 같아지는 순간 찾기
ans = -1
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)