n = int(input())
students = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    student = [n_i, int(h_i), int(w_i)]
    students.append(student)

# 키를 기준으로 오름차순 정렬
    # 키가 동일한 경우 몸무게를 기준으로 내림차순
students.sort(key=lambda x : (x[1], -x[2]))

for s in students:
    print(*s)