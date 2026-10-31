class Student:
    def __init__(self, n, k, e, m):
        self.n = n
        self.k = k
        self.e = e
        self.m = m
    
    def show_score(self):
        print(self.n, self.k, self.e, self.m)

n = int(input())

students = []

for _ in range(n):
    name, korean, english, math = input().split()
    student = Student(name, int(korean), int(english), int(math))
    students.append(student)

# 정렬 국 - 영 - 수
students.sort(key=lambda x: (-x.k, -x.e, -x.m))

for s in students:
    print(s.n, s.k, s.e, s.m)