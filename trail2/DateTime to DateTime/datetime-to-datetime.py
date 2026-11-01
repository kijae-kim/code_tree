a, b, c = map(int, input().split())

# 시작 시간과 목표 시간을 총 분(Minute)으로 변환
start_total = 11 * 24 * 60 + 11 * 60 + 11
target_total = a * 24 * 60 + b * 60 + c

ans = target_total - start_total

# 목표 시간이 시작 시간보다 앞서는 경우
if ans < 0:
    print(-1)
else:
    print(ans)