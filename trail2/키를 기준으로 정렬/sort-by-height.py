class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

group = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    student = Student(n_i, int(h_i), int(w_i))
    group.append(student)

# 키를 기준으로 오름차순 정렬.
group.sort(key=lambda x:x.height)

for student in group:
    print(student.name, student.height, student.weight)