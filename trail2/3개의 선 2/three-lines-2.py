DIM = 10  # 문제 조건에 맞게 좌표 범위를 0~10으로 설정합니다.

n = int(input())
points = []
x_arr = [0] * (DIM + 1)
y_arr = [0] * (DIM + 1)

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    x_arr[x] += 1
    y_arr[y] += 1

# 점을 커버할 수 있는지 확인하는 함수 (DFS 활용)
def check(line_idx, selected):
    # 선을 3개 골랐을 때 모든 점이 커버되는지 검사
    if line_idx == 3:
        for px, py in points:
            covered = False
            for type, coord in selected:
                if type == 'x' and px == coord:
                    covered = True
                    break
                if type == 'y' and py == coord:
                    covered = True
                    break
            if not covered:
                return False
        return True

    # 0부터 10까지의 위치 중 가로선 또는 세로선을 골라봄
    for i in range(DIM + 1):
        # 1. 세로선(x = i)을 선택하는 경우
        selected.append(('x', i))
        if check(line_idx + 1, selected):
            return True
        selected.pop()

        # 2. 가로선(y = i)을 선택하는 경우
        selected.append(('y', i))
        if check(line_idx + 1, selected):
            return True
        selected.pop()

    return False

# 탐색 시작 (고른 선의 개수: 0개, 선택 리스트: 빈 리스트)
if check(0, []):
    print(1)
else:
    print(0)