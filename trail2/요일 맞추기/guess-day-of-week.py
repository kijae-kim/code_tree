m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_name = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# 1월 1일부터 해당 월-일까지의 총 일수를 계산하는 함수
def get_total_days(m, d):
    total = d
    for i in range(1, m):
        total += num_of_days[i]
    return total

total1 = get_total_days(m1, d1)
total2 = get_total_days(m2, d2)

# 두 날짜의 일수 차이
diff = total2 - total1

# m1월 d1일이 월요일(인덱스 1)이므로, 차이만큼 더한 후 7로 나눈 나머지 계산
# (파이썬의 % 연산자는 음수도 올바르게 처리합니다)
target_index = (1 + diff) % 7

print(day_name[target_index])