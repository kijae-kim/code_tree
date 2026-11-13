n = int(input())
A = list(map(int, input().split()))


# i번째 집에는 A명의 사람이 살고 있어.
# N개의 집 중 한 집에 모여야해.

# 출력
# 사람들의 이동 거리의 합이 최소가 되도록한다.
ans = float('inf')

for i in range(n):
    # i번째 집에서 모인다
    distance = 0
    for j in range(n):
        gap = abs(i - j)
        distance += (A[j]*gap)
    ans = min(distance, ans)

print(ans)