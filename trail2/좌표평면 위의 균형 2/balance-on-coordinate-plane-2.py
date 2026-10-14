n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 가장 많은 점의 수가 최소가 되도록 한다.
# 가장 많은 점이 있는 구역의 점의 개수 M개
# 가능한 최솟값 M을 구하는 것
# x와 y의 후보가 될 수 있는 수는 0초과 100미만의 짝수이다.
x_hubo = list(range(2, 100, 2))
y_hubo = list(range(2, 100, 2))

ans = float("inf")
cnt = 0
for x_line in x_hubo:
    for y_line in y_hubo:
        # 새로운 직선 조합이 시작될 때마다 카운터 초기화
        q1, q2, q3, q4 = 0, 0, 0, 0
        
        # 모든 점을 돌며 어느 구역인지 카운트
        for px, py in points:
            # q1 : x > hubo & y > hubo
            if px > x_line and py > y_line:
                q1 += 1
            # q2 : x < hubo & y > hubo
            elif px < x_line and py > y_line:
                q2 += 1
            # q3 : x < hubo & y < hubo
            elif px < x_line and py < y_line:
                q3 += 1
            # q2 : x > hubo & y < hubo
            elif px > x_line and py < y_line:
                q4 += 1
                
        # 현재 직선 조합에서의 최댓값 구하기
        current_max = max(q1, q2, q3, q4)
        
        # 전체 최솟값(ans) 갱신하기
        ans = min(ans, current_max)

print(ans)