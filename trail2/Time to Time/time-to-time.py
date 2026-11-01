s_h, s_m, e_h, e_m = map(int, input().split())

# 2시 5분 시작
# 4시 1분 끝

elapsed_time = 0 

hour = s_h
mins = s_m

while True:
    # 종료조건
    if hour == e_h and mins == e_m:
        break

    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_time)