n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0


# 특정 위치(r, c)에서 시작하는 1x3 직사각형의 동전 합을 구하는 함수
def get_sum(r, c):
  return grid[r][c] + grid[r][c + 1] + grid[r][c + 2]


# 1. 첫 번째 직사각형 위치 탐색 (r1, c1)
for r1 in range(n):
  for c1 in range(n - 2):
    sum1 = get_sum(r1, c1)

    # 2. 두 번째 직사각형 위치 탐색 (r2, c2)
    for r2 in range(n):
      for c2 in range(n - 2):

        # 만약 두 직사각형이 같은 행에 있다면, 열이 겹치는지 확인
        if r1 == r2:
          # 두 직사각형의 열 범위가 겹치면 겹침 (스킵)
          # c1 ~ c1+2 와 c2 ~ c2+2 가 겹치지 않으려면
          # c1 + 3 <= c2 또는 c2 + 3 <= c1 이어야 함
          if not (c1 + 3 <= c2 or c2 + 3 <= c1):
            continue

        sum2 = get_sum(r2, c2)
        ans = max(ans, sum1 + sum2)

print(ans)