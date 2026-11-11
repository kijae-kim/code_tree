n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

point = k - 1
if point // n == 0:
    i = point // n
    j = point % n
    dir = "S"
elif point // n == 1:
    i = point % n
    j = n - 1
    dir = "W"
elif point // n == 2:
    i = n - 1
    j = n - (point % n) - 1
    dir = "N"
elif point // n == 3:
    i = n - (point % n) - 1
    j = 0
    dir = "E"

ans = 0

# 격자 범위를 벗어날 때까지 반복
while 0 <= i < n and 0 <= j < n:
    cell = grid[i][j]

    if dir == "S":
        if cell == "\\":
            ans += 1
            dir = "E"
            j += 1
        elif cell == "/":
            ans += 1
            dir = "W"
            j -= 1
    elif dir == "E":
        if cell == "\\":
            ans += 1
            dir = "S"
            i += 1
        elif cell == "/":
            ans += 1
            dir = "N"
            i -= 1
    elif dir == "W":
        if cell == "\\":
            ans += 1
            dir = "N"
            i -= 1
        elif cell == "/":
            ans += 1
            dir = "S"
            i += 1
    elif dir == "N":
        if cell == "\\":
            ans += 1
            dir = "W"
            j -= 1
        elif cell == "/":
            ans += 1
            dir = "E"
            j += 1

print(ans)