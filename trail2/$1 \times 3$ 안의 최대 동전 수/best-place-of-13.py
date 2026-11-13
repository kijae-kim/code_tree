n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# [0] * 3, 크기의 직사각형 필터
# 해당 범위 안에 들어 있는 동전의 개수를 최대로

ans = 0

for i in range(n):
    for j in range(n-2):
        box = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        ans = max(ans, box)

print(ans)