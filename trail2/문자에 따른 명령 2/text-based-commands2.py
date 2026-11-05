dirs = input()

# Please write your code here.
# North를 바라본 상태로 출발
N = len(dirs)

x, y = 0, 0
degree = 90  # 90: North, 0: West, 180: East, 270 (or -90): South

for i in range(N):
    d = dirs[i]

    if d == 'L':
        degree = (degree - 90) % 360
    elif d == 'R':
        degree = (degree + 90) % 360
    elif d == 'F':
        # Normalize negative degrees if any (e.g., -90 -> 270)
        norm_degree = degree % 360
        
        if norm_degree == 90:
            y += 1
        elif norm_degree == 0:
            x -= 1
        elif norm_degree == 180:
            x += 1
        elif norm_degree == 270:
            y -= 1

print(x, y)