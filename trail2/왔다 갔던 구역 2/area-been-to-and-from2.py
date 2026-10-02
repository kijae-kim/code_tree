OFFSET = 1000
MAX = 2000

N = int(input())

current = 0
sections = []

for _ in range(N):
    x, dir = tuple(input().split())
    x = int(x)
    # 왼쪽으로 이동하면  cur - x
    if dir == "L":
        start = current - x
        end = current
        current -= x
    
    elif dir == "R":
        start = current
        end = current + x
        current += x
    
    sections.append([start, end])

LINES = [0] * (MAX+1)

for s, e in sections:
    s, e = s + OFFSET, e + OFFSET

    for k in range(s,e):
        LINES[k] += 1

cnt = 0
for char in LINES:
    if char >= 2:
        cnt += 1
print(cnt)