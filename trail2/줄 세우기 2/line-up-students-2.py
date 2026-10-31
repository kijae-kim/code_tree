n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# 조건에 따라 정렬: 키 오름차순(x[0]), 몸무게 내림차순(-x[1])
students.sort(key=lambda x: (x[0], -x[1]))

# 정렬된 결과 출력 (키, 몸무게, 번호)
for student in students:
  print(*student)