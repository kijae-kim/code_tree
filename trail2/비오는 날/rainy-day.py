class Program:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
date = []
day = []

program = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    program.append(Program(d, dy, w))

# 1. 날씨가 'Rain'인 객체들만 필터링
rainy_programs = [p for p in program if p.weather == 'Rain']

# 2. 그 중 date(날짜)가 가장 빠른(작은) 객체 찾기
ans = min(rainy_programs, key=lambda x: x.date)

# 3. 결과 출력
print(f"{ans.date} {ans.day} {ans.weather}")