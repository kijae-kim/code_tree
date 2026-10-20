n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


# 2 <= N <= 10
# 1 <= M <= 100
# m번

max_cnt = -float("inf")
tmp = {}

for i in range(m):
    items = tmp.items()
    a, b = pairs[i]
    # a가 더 크면 위치 바꿔
    if a > b:
        a, b = b, a
    # 이미 범위쌍이 dict에 있으면 val += 1
    if (a,b) in tmp:
        tmp[(a,b)] = tmp.get((a,b)) + 1
    else:
        tmp.setdefault((a,b), 1)

ans = tmp.values()
print(max(ans))