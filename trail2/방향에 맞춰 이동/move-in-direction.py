n = int(input())
moves = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
x = 0
y = 0

# 이동명령을 받아
for i in range(n):
    # 방향, 얼마나 움직일건지
    dir, M = moves[i][0], int(moves[i][1])
    if dir == 'W':
        y = y - M
    elif dir == 'E':
        y = y + M
    elif dir == 'N':
        x = x + M
    elif dir == 'S':
        x = x - M

print(y, x)