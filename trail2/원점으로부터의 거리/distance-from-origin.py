n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# 원점에서 가까운 점부터 순서대로 번호를 출력
    # 거리가 같은 점이 여러 개인 경우, 
        # 번호가 작은 점 부터 출력

def manhatan(x, y):
    ans = abs(x-0) + abs(y-0)
    return ans

points.sort(key=lambda x : manhatan(x[1][0], x[1][1]))

for i in range(n):
    print(points[i][0]+1)