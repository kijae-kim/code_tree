m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

# 2024년은 윤년이므로 2월이 29일까지 있음
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 시작일(m1, d1)의 요일을 찾기 위해 1월 1일부터의 총 일수 차이 계산
# 문제에서 m1월 d1일이 월요일(인덱스 0)이라고 주어졌으므로 기준을 맞춤
def get_total_days(m, d):
    total = d
    for i in range(1, m):
        total += num_of_days[i]
    return total

start_total = get_total_days(m1, d1)
target_total = get_total_days(m2, d2)

# 날짜를 하루씩 이동하며 요일 카운트
count = 0
current_m, current_d = m1, d1

# m1월 d1일이 월요일(day_name의 인덱스 0)로 시작하므로,
# 1월 1일 기준 날짜 차이를 이용해 현재 요일 인덱스 계산
day_index = (get_total_days(current_m, current_d) - start_total) % 7

while True:
    # 현재 요일이 찾고자 하는 요일과 같다면 카운트 증가
    if day_name[day_index] == target_day:
        count += 1
        
    # 목표 날짜에 도달했으면 반복 종료
    if current_m == m2 and current_d == d2:
        break
        
    # 다음 날로 이동
    current_d += 1
    day_index = (day_index + 1) % 7
    
    if current_d > num_of_days[current_m]:
        current_m += 1
        current_d = 1

print(count)