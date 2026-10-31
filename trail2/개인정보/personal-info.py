n = 5
students = []

for _ in range(n):
    n, h, w = input().split()
    student = [n, int(h), float(w)]
    students.append(student)
# 이름순 정렬하여 출력
students.sort(key=lambda x : x[0])
print("name")
for s in students:
    print(*s)

print()
# 키가 큰 순으로 정렬
students.sort(key=lambda x : -x[1])
print("height")
for s in students:
    print(*s)