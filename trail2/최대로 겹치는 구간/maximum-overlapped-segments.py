OFFSET = 100
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

lines = [0] * (OFFSET*2 + 5)

for i in range(n):
    l, r = segments[i]
    for p in range(l,r):
        lines[p] += 1

print(max(lines))