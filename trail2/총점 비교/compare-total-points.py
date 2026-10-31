class Student:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3


n = int(input())
students = []

for _ in range(n):
    name, s1, s2, s3 = input().split()
    student = Student(name, int(s1), int(s2), int(s3))
    students.append(student)

# 학생들을 세 과목의 총점이 낮은 순으로 정렬하여 출력
students.sort(key=lambda x: (x.s1 + x.s2 + x.s3))

for s in students:
    print(s.name, s.s1, s.s2, s.s3)