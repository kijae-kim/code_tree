n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
# 튜플 형으로 키 값을 정렬
students.sort(key=lambda x: (-x[0], -x[1], x[2]))

# 다음으로 키와 몸무게가 동일하다면 번호가 작은 학생이 앞에 올 수 있도록 설정
for s in students:
    print(*s)