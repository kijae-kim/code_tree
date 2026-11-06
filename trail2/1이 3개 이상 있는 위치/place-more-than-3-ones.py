n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 상하좌우에 1이 3개 이상 있는 경우 (본인은 제외임)

tmp_list = []
ans = 0

for i in range(n):
    for j in range(n):
        # 상하좌우 체크
        cnt = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                cnt += 1

        if cnt >= 3:
            ans += 1
            tmp_list.append((i, j))
# print(tmp_list)
print(ans)
