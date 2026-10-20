n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
# 2*x

tmp = []

MAX_NUM = max(max(a), max(b))

for x in range(1, MAX_NUM+1):
    correct = 0
    for i in range(n):
        hubo = 2**(i+1) * x
        if a[i] <= hubo <= b[i]:
            correct += 1
    if correct == n:
        tmp.append(x)

ans = min(tmp)
print(ans)