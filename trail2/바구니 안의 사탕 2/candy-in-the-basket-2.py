N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# 사탕의 개수가 최대
# [c - K, c + K] 구간

L = max(pos)

ans = 0

for c in range(L + 1):
    MIN = c - K
    MAX = c + K
    current_sum = 0

    for i in range(N):
        if MIN <= pos[i] <= MAX:
            current_sum += candy[i]

    ans = max(ans, current_sum)

print(ans)
