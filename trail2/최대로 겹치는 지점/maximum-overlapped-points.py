n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
MAX = 100
lines = [0] * (MAX+1)

for i in range(n):
    l, r = segments[i]
    for p in range(l, r+1):
        lines[p] += 1

print(max(lines))
