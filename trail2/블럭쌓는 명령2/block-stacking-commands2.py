n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

lines = [0] * n

for i, j in commands:
    for k in range(i-1, j):
        lines[k] += 1

print(max(lines))