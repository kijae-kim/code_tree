def solve():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # 1. 모든 체크포인트를 순서대로 방문할 때의 기본 총 거리 계산
    total_dist = 0
    for i in range(n - 1):
        total_dist += abs(points[i][0] - points[i+1][0]) + abs(points[i][1] - points[i+1][1])

    min_dist = float('inf')

    # 2. 2번째부터 N-1번째 체크포인트(인덱스 1부터 n-2) 중 하나를 건너뛰어봄
    for i in range(1, n - 1):
        # i번째 체크포인트를 방문하지 않을 때 빠지는 거리 (i-1 -> i -> i+1)
        removed = (
            abs(points[i-1][0] - points[i][0]) + abs(points[i-1][1] - points[i][1]) +
            abs(points[i][0] - points[i+1][0]) + abs(points[i][1] - points[i+1][1])
        )
        # i번째를 건너뛰면서 새로 생기는 거리 (i-1 -> i+1)
        added = abs(points[i-1][0] - points[i+1][0]) + abs(points[i-1][1] - points[i+1][1])
        
        # 이번 체크포인트를 건너뛰었을 때의 총 거리
        current_total = total_dist - removed + added
        
        if current_total < min_dist:
            min_dist = current_total

    print(min_dist)

solve()